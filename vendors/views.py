from django.shortcuts import render
from django.shortcuts import render
from .models import Vendor, ActivationProcess

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


def activation_process_status(request):
    # Query all vendors with their activation process status
    vendors = Vendor.objects.select_related('activation_process').all()

    # Group vendors by activation process status
    status_groups = {
        'Email Sent': vendors.filter(activation_process__status='email'),
        'Identify Contact Person': vendors.filter(activation_process__status='identify_contact_person'),
        'Items Analysis': vendors.filter(activation_process__status='items_analysis'),
        'Gain Stock List': vendors.filter(activation_process__status='gain_stock_list'),
        'Activated': vendors.filter(activation_process__status='activated'),
        'Lost': vendors.filter(activation_process__status='lost'),
    }

    context = {
        'status_groups': status_groups,
    }

    return render(request, 'activation_process_status.html', context)
