from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator
from django.template.defaultfilters import slugify
import math


class Categories(models.Model):
    """Model for Equipment Categories"""
    category = models.CharField(max_length=25, unique=True)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.category


class Equipment(models.Model):
    """Model for Equipment"""
    make_and_model = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="equipment_user")
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,
                                 related_name="equipment_category")
    vibration_magnitude = models.FloatField()
    test_date = models.DateField()
    equipment_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'make_and_model']

    def __str__(self):
        return self.make_and_model

    """
    Source: https://github.com/veryacademy/YT-Django-CBV-Mini-Series/
    blob/master/CreateView/books/models.py
    """
    def save(self, *args, **kwargs):
        """Creates unique slug based on the instances make_and_model"""
        if not self.slug:
            self.slug = slugify(self.make_and_model)
        return super().save(*args, **kwargs)

    def exp_pts_per_hour(self):
        """Calculates the instances Exposure Points per Hour"""
        eav = float(2.5)
        per_hour = float(0.125)
        exp_pts = (self.vibration_magnitude / eav) ** 2 * per_hour * 100
        exp_pts_per_hour = math.trunc(exp_pts)
        return exp_pts_per_hour

    def time_to_eav(self):
        """
        Calculates the instances Time to Reach Exposure Action Value (EAV)
        """
        eav = float(2.5)
        time_to_eav = (eav / self.vibration_magnitude) ** 2 * 8
        time_to_eav_hours = math.trunc(time_to_eav)
        time_to_eav_minutes = math.trunc(60
                                         * (time_to_eav - time_to_eav_hours))
        return f"{time_to_eav_hours} Hours {time_to_eav_minutes} Minutes"

    def time_to_elv(self):
        """Calculates the instances Time to Reach Exposure Limit Value (EAV)"""
        elv = float(5)
        time_to_elv = (elv / self.vibration_magnitude) ** 2 * 8
        time_to_elv_hours = math.trunc(time_to_elv)
        time_to_elv_minutes = math.trunc(60
                                         * (time_to_elv - time_to_elv_hours))
        return f"{time_to_elv_hours} Hours {time_to_elv_minutes} Minutes"


class Calculator(models.Model):
    """Model for Users Calculators"""
    make_and_model = models.ForeignKey(Equipment, on_delete=models.CASCADE,
                                       related_name="equipment_make_and_model")
    slug = models.SlugField(max_length=80, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="calculator_user")
    exposure_duration_hours = models.IntegerField(
        default=0, validators=[MaxValueValidator(23)]
        )
    exposure_duration_minutes = models.IntegerField(
        default=0, validators=[MaxValueValidator(59)]
        )

    class Meta:
        ordering = ['make_and_model']

    def __str__(self):
        return f"""{self.make_and_model} used for
                 {self.exposure_duration_hours} hours and
                 {self.exposure_duration_minutes} minutes"""

    """
    Source: https://github.com/veryacademy/YT-Django-CBV-Mini-Series/
    blob/master/CreateView/books/models.py
    Source for get_random_string: https://stackoverflow.com/questions/42429463/
    django-generating-random-unique-slug-field-for-each-model-object
    """
    def save(self, *args, **kwargs):
        """
        Creates unique slug based on the instances author, make_and_model, and
        exposure duration. A random string is included on the end to prevent
        error when a duplicate instances is added.
        """
        if not self.slug:
            self.slug = slugify(f"""{self.author}-{self.make_and_model}-
                                {self.exposure_duration_hours}-
                                {self.exposure_duration_minutes}-
                                {get_random_string(5)}""")
        return super().save(*args, **kwargs)

    def partial_exposure(self):
        """Calculates the instances Partial Exposure"""
        eav = float(2.5)
        exp_hours = float(self.exposure_duration_hours)
        exp_mins = float(self.exposure_duration_minutes) / 60
        exp_time = float(math.sqrt((exp_hours + exp_mins) / 8))
        partial_exp = self.make_and_model.vibration_magnitude * exp_time
        partial_exp = round(partial_exp, 1)
        return partial_exp

    def partial_exposure_pts(self):
        """Calculates the instances Partial Exposure Points"""
        eav = float(2.5)
        exp_hours = float(self.exposure_duration_hours)
        exp_mins = float(self.exposure_duration_minutes) / 60
        exp_time = (exp_hours + exp_mins) / 8
        exp_pts = (self.make_and_model.vibration_magnitude
                   / eav) ** 2 * exp_time * 100
        partial_exp_pts = math.trunc(exp_pts)
        return partial_exp_pts
