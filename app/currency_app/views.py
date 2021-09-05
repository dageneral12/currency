from django.urls import reverse_lazy

from .models import Rate, ContactUs, Source

from django.core.mail import send_mail

from django.conf import settings

from django.views.generic import (CreateView,
                                  UpdateView,
                                  DeleteView,
                                  DetailView,
                                  ListView)
from django.shortcuts import render, redirect, get_object_or_404
from currency_app.forms import SourceForm, RateForm, ContactUsForm


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
        contact_request = ContactUsForm(request.POST)
        if contact_request.is_valid():
            contact_request.save()
            return redirect('filter_messages')

        else:
            return redirect('filter_messages')


def show_sources(request):
    sources = Source.objects.all()
    return render(request,
                  'show_sources.html',
                  {'sources': sources})


def rate_create(request):
    if request.method == 'POST':
        create_form = RateForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('rate_list')
    elif request.method == 'GET':
        create_form = RateForm()

    return render(request, 'rate_create.html', {'create_form': create_form})


def rate_delete(request, rate_id):

    rate = get_object_or_404(Rate, id=rate_id)
    rate_form = RateForm(instance=rate)

    if request.method == 'POST':
        rate_form = RateForm(request.POST, instance=rate)

        rate.delete()
        return redirect('rate_list')
    return render(request, 'rate_delete.html', {'rate_form': rate_form})


def rate_details(request, rate_id):
    rate = get_object_or_404(Rate, id=rate_id)
    return render(request, 'rate_detail.html', {'rate': rate})


def rate_update(request, rate_id):
    rate = get_object_or_404(Rate, id=rate_id)
    if request.method == 'POST':
        rate_form = RateForm(request.POST, instance=rate)
        if rate_form.is_valid():
            rate_form.save()
            return redirect('rate_list')
    elif request.method == 'GET':
        rate_form = RateForm(instance=rate)

    return render(request, 'rate_update.html', {'rate_form': rate_form})


# Homework 8 & 9 - Class based views, Source, reverse


class SourceListView(ListView):

    model = Source
    template_name = 'show_sources.html'


class SourceCreateView(CreateView):
    model = Source
    template_name = 'source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('source_list')


class SourceDetailView(DetailView):

    queryset = Source.objects.all()
    template_name = 'source_details.html'
    context_object_name = 'detail_view'


class SourceDeleteView(DeleteView):

    queryset = Source.objects.all()
    form_class = SourceForm
    template_name = 'source_delete.html'
    success_url = reverse_lazy('source_list')
    context_object_name = 'del_view'


class SourceUpdateView(UpdateView):

    queryset = Source.objects.all()
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy('source_list')
    context_object_name = 'update_view'


class ContactUsCreateView(CreateView):

    model = ContactUs
    success_url = reverse_lazy('filter_messages')
    template_name = 'contact_us_form.html'
# form = ContactUsForm - no need to mention the form,
# can copy fields from the model only (see below:)
    fields = (
        'email_from',
        'subject',
        'message',
        )

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        email_from = form.cleaned_data['email_from']
        full_email_body = f'''Email from: {email_from} /n
        Body: {message}'''
        send_mail(
            subject,
            full_email_body,
            settings.EMAIL_HOST_USER,  # your from address
            ['dageneral@gmail.com'],  # list of to addresses
            fail_silently=False,
            )
        return super().form_valid(form)
