from django.test import TestCase
from django.contrib.auth import get_user_model
from calculator.models import Categories, Equipment, Calculator

# Add tests such as for models.CharField(max_length=50, unique=True)
# update john lennon


class TestModels(TestCase):
    """Tests Models"""
    def setUp(self):
        """
        Sets up the user and models for the tests
        """
        User = get_user_model()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')

        self.category = Categories.objects.create(
            category='Breaker',
        )

        self.equipment = Equipment.objects.create(
            make_and_model='equipment1',
            author=self.user,
            updated_on='2023-01-23',
            category=self.category,
            vibration_magnitude=5.5,
            test_date='2023-01-23',
            equipment_image='placeholder',
        )

        self.calculator = Calculator.objects.create(
            make_and_model=self.equipment,
            author=self.user,
            slug='john-equipment1-1-30-8a1xu',
            exposure_duration_hours=1,
            exposure_duration_minutes=30,
        )

    def test_equipment_slug_is_assigned(self):
        """
        Tests whether a slug is being assigned and that it is the correct one
        """
        self.assertEquals(self.equipment.slug, "equipment1")

    def test_exp_pts_per_hour(self):
        """
        Tests Exposure Points per Hour returns correct value
        """
        self.exp_pts_per_hour = self.equipment.exp_pts_per_hour()
        self.assertEquals(self.exp_pts_per_hour, 60)

    def test_time_to_eav(self):
        """
        Tests Time to EAV returns correct value
        """
        self.time_to_eav = self.equipment.time_to_eav()
        self.assertEquals(self.time_to_eav, "1 Hours 39 Minutes")

    def test_time_to_elv(self):
        """
        Tests Time to ELV returns correct value
        """
        self.time_to_elv = self.equipment.time_to_elv()
        self.assertEquals(self.time_to_elv, "6 Hours 36 Minutes")

    def test_partial_exposure(self):
        """
        Tests Partial Exposure returns correct value
        """
        self.partial_exposure = self.calculator.partial_exposure()
        self.assertEquals(self.partial_exposure, 2.4)

    def test_partial_exposure_pts(self):
        """
        Tests Partial Exposure Points returns correct value
        """
        self.partial_exposure_pts = self.calculator.partial_exposure_pts()
        self.assertEquals(self.partial_exposure_pts, 90)
