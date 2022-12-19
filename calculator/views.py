from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Equipment, Calculator
from .forms import CalculatorForm, EquipmentForm


def Index(request):
    return render(request, 'index.html', {})


# Calculator Views


class CalculatorListView(generic.ListView):
    model = Calculator
    queryset = Calculator.objects.order_by('make_and_model')
    template_name = 'calculator.html'

    # Source: @Ed B_alum CI Project-Portfolio-4 Slack Channel
    def get_queryset(self):
        queryset = super(CalculatorListView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


class CalculatorCreateView(generic.CreateView):
    model = Calculator
    form_class = CalculatorForm
    template_name = 'add-calculator.html'
    success_url = '/calculator/'

    # Source: https://stackoverflow.com/questions/72033344/set-the-logged-in-user-to-created-by-for-django-createview
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CalculatorEditView(generic.UpdateView):
    model = Calculator
    form_class = CalculatorForm
    template_name = 'edit-calculator.html'
    success_url = '/calculator/'


class CalculatorDeleteView(generic.DeleteView):
    model = Calculator
    template_name = 'delete-calculator.html'
    success_url = '/calculator/'


# Source https://www.codegrepper.com/tpc/how+to+delete+all+instances+of+model+in+django
def DeleteAll(request):
    Calculator.objects.filter(author=request.user).delete()
    context = {}
    return render(request, 'calculator.html', context)


# Equipment Views


class EquipmentListView(generic.ListView):
    model = Equipment
    queryset = Equipment.objects.all()
    template_name = 'equipment.html'
    paginate_by = 6


class EquipmentDetail(View):

    def get(self, request, slug, *args, **kwargs):
        equipment_info = Equipment.objects.all()
        equipment = get_object_or_404(equipment_info, slug=slug)

        return render(
            request,
            "equipment-detail.html",
            {'equipment': equipment},
        )
