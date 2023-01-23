from django.test import SimpleTestCase
from django.urls import reverse, resolve
from calculator.views import Index, CalculatorListView, CalculatorDetail, CalculatorCreateView, CalculatorEditView, CalculatorDeleteView, DeleteAll, EquipmentListView, EquipmentDetail


class TestUrls(SimpleTestCase):
    """Test URLs"""
    def test_index_url_is_resolved(self):
        """Test Index URL"""
        url = reverse('index')
        self.assertEquals(resolve(url).func, Index)

    def test_calculator_list_url_is_resolved(self):
        """Test Calcualtor List URL"""
        url = reverse('calculator_list')
        self.assertEquals(resolve(url).func.view_class, CalculatorListView)

    def test_calculator_detail_url_is_resolved(self):
        """Test Calcualtor Detail URL"""
        url = reverse('calculator_detail', args=['calculator-id'])
        self.assertEquals(resolve(url).func.view_class, CalculatorDetail)

    def test_calculator_create_url_is_resolved(self):
        """Test Calcualtor Create URL"""
        url = reverse('add_calculator')
        self.assertEquals(resolve(url).func.view_class, CalculatorCreateView)

    def test_calculator_edit_url_is_resolved(self):
        """Test Calcualtor Edit URL"""
        url = reverse('edit_calculator', args=['calculator-id'])
        self.assertEquals(resolve(url).func.view_class, CalculatorEditView)

    def test_calculator_delete_url_is_resolved(self):
        """Test Calcualtor Delete URL"""
        url = reverse('delete_calculator', args=['calculator-id'])
        self.assertEquals(resolve(url).func.view_class, CalculatorDeleteView)

    def test_delete_all_url_is_resolved(self):
        """Test Delete All URL"""
        url = reverse('delete_all')
        self.assertEquals(resolve(url).func, DeleteAll)

    def test_equipment_list_url_is_resolved(self):
        """Test Equipment List URL"""
        url = reverse('equipment_list')
        self.assertEquals(resolve(url).func.view_class, EquipmentListView)

    def test_equipment_detail_url_is_resolved(self):
        """Test Equipment Detail URL"""
        url = reverse('equipment_detail', args=['equipment-id'])
        self.assertEquals(resolve(url).func.view_class, EquipmentDetail)
