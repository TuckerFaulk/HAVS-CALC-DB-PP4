from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Equipment, Calculator
# from .forms import CalculatorForm, EquipmentForm


def Index(request):
    return render(request, 'index.html', {})


class CalculatorListView(generic.ListView):
    model = Calculator
    queryset = Calculator.objects.order_by('make_and_model')
    template_name = 'calculator.html'


# Equipment Views 
# Line 34 - .objects.filter(user=request.user)


class EquipmentListView(generic.ListView):
    model = Equipment
    queryset = Equipment.objects.filter(approved=True)
    template_name = 'equipment.html'


class EquipmentDetail(View):

    def get(self, request, slug, *args, **kwargs):
        equipment_info = Equipment.objects.all()
        equipment = get_object_or_404(equipment_info, slug=slug)

        return render(
            request,
            "equipment-detail.html",
            {'equipment': equipment},
        )
