from django.shortcuts import render, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import generic, View
from .models import Equipment, Calculator
from .forms import CalculatorForm, EquipmentForm


def Index(request):
    """View which displays the home page"""
    return render(request, 'index.html', {})


# Calculator Views


class CalculatorListView(generic.ListView):
    """
    View which displays the calculator. The view is
    filtered by userso they can only see the equipment
    which they have added.
    """
    model = Calculator
    queryset = Calculator.objects.order_by('make_and_model')
    template_name = 'calculator.html'

    # Source: @Ed B_alum CI Project-Portfolio-4 Slack Channel
    def get_queryset(self):
        queryset = super(CalculatorListView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


class CalculatorDetail(View):
    """View which displays the calculator equipment details"""
    def get(self, request, slug, *args, **kwargs):
        calculator_info = Calculator.objects.all()
        calculator = get_object_or_404(calculator_info, slug=slug)

        return render(
            request,
            "calculator-detail.html",
            {'calculator': calculator},
        )


class CalculatorCreateView(messages.views.SuccessMessageMixin,
                           generic.CreateView):
    """View which displays a form to add equipment to the calculator"""
    model = Calculator
    form_class = CalculatorForm
    template_name = 'add-calculator.html'
    success_url = '/calculator/'
    success_message = "Equipment successfully added!"

    """
    Source: https://stackoverflow.com/questions/72033344/
    set-the-logged-in-user-to-created-by-for-django-createview
    """
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CalculatorEditView(messages.views.SuccessMessageMixin,
                         generic.UpdateView):
    """
    View which displays a form to edit equipment
    details in the calculator
    """
    model = Calculator
    form_class = CalculatorForm
    template_name = 'edit-calculator.html'
    success_url = '/calculator/'
    success_message = "Equipment successfully edited!"


class CalculatorDeleteView(generic.DeleteView):
    """
    View which displays a page to request user to
    confirm they are deleting equipment from their calculator
    """
    model = Calculator
    template_name = 'delete-calculator.html'
    success_url = '/calculator/'
    success_message = "Equipment was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CalculatorDeleteView, self).delete(request, *args,
                                                        **kwargs)


"""
Source https://www.codegrepper.com/tpc/
how+to+delete+all+instances+of+model+in+django
"""


def DeleteAll(request):
    """
    View which deletes all equipment from a users
    calculator
    """
    Calculator.objects.filter(author=request.user).delete()
    messages.add_message(request, messages.SUCCESS, """You have
                         successfully reset your calculator!""")
    context = {}
    return render(request, 'calculator.html', context)


# Equipment Views


class EquipmentListView(generic.ListView):
    """View which displays a list of equipment"""
    model = Equipment
    queryset = Equipment.objects.all()
    template_name = 'equipment.html'
    paginate_by = 6


class EquipmentDetail(View):
    """View which displays equipment details"""
    def get(self, request, slug, *args, **kwargs):
        equipment_info = Equipment.objects.all()
        equipment = get_object_or_404(equipment_info, slug=slug)

        return render(
            request,
            "equipment-detail.html",
            {'equipment': equipment},
        )
