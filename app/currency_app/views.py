from .models import Rate, ContactUs

from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .forms import ContactForm


# Create your views here.
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('Hello World!')


def rate_list(request):
    rates = Rate.objects.all()
    return render(request, 'rate_page.html', {'rates': rates, })


def filter_contact_us_msg(request):
    msgs_filtered = ContactUs.objects.all()

    return render(request,
                  'contact_details.html',
                  {'msgs_filtered': msgs_filtered})


def contact_us_form(request):
    if request.method == 'POST':
        contact_request = ContactForm(request.POST)
        if contact_request.is_valid():
            contact_request.save()
            return redirect('filter_messages')

        else:
            return render()


class Create_View(CreateView):

    model = Rate
