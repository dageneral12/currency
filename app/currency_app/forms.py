from django import forms
from .models import ContactUs, Rate, Source


class SourceForm(forms.ModelForm):

    class Meta:

        model = Source
        fields = ('name', 'source_url')


class RateForm(forms.ModelForm):

    class Meta:

        model = Rate


        fields = ('sale', 'buy', 'source', 'currency')


class ContactUsForm(forms.ModelForm):

    class Meta:

        model = ContactUs
        fields = ('email_from', 'subject', 'message')
