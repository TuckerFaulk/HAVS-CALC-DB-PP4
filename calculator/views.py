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


# .filter(author=user)