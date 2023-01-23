from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from calculator.models import Categories, Equipment, Calculator

# Add Documentation, Consider POST Tests, checking info displayed on DOM
# Redirecting to the Calculator after adding equipment


class TestViews(TestCase):

    def setUp(self):
        """
        Sets up the user and models for the tests
        """

        User = get_user_model()
        self.client = Client()
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
            vibration_magnitude='1.0',
            test_date='2023-01-23',
            equipment_image='placeholder',
        )

        Calculator.objects.create(
            make_and_model=self.equipment,
            author=self.user,
            slug='john-equipment1-1-30-8a1xu',
            exposure_duration_hours='1',
            exposure_duration_minutes='30',
        )

        self.index_url = reverse('index')
        self.calculator_list_url = reverse('calculator_list')
        self.calculator_detail_url = reverse('calculator_detail', args=['john-equipment1-1-30-8a1xu'])
        self.calculator_create_url = reverse('add_calculator')
        self.calculator_edit_url = reverse('edit_calculator', args=['john-equipment1-1-30-8a1xu'])
        self.calculator_delete_url = reverse('delete_calculator', args=['john-equipment1-1-30-8a1xu'])
        self.calculator_delete_all_url = reverse('delete_all')
        self.equipment_list_url = reverse('equipment_list')
        self.equipment_detail_url = reverse('equipment_detail', args=['equipment1'])

    def test_index(self):
        """
        Successfully loading the Index View
        """
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_calculator_list_GET(self):
        """
        Successfully loading the Calculator View
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.calculator_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'calculator.html')

    def test_calculator_detail_GET(self):
        """
        Successfully loading the Calculator Detail View
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.calculator_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'calculator-detail.html')

    def test_calculator_create_GET(self):
        """
        Successfully loading the Add Calculator View
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.calculator_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add-calculator.html')

    def test_calculator_edit_GET(self):
        """
        Successfully loading the Edit Calculator View
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.calculator_edit_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit-calculator.html')

    def test_calculator_delete_GET(self):
        """
        Successfully loading the Delete Calculator View
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.calculator_delete_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete-calculator.html')

    def test_calculator_delete_all_GET(self):
        """
        Successfully loading the Delete All View
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.calculator_delete_all_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'calculator.html')

    def test_equipment_list_GET(self):
        """
        Successfully loading the Equipment List View
        """
        response = self.client.get(self.equipment_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'equipment.html')

    def test_equipment_detail_GET(self):
        """
        Successfully loading the Equipment Detail View
        """
        response = self.client.get(self.equipment_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'equipment-detail.html')
