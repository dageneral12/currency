from django import forms
from .models import ContactUs, Rate, Source


class SourceForm(forms.ModelForm):

    class Meta:

        model = Source
        fields = ('name', 'source_url')

    def get_data(self):
        return Source.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        all_sources = self.get_data()
        name_cleaned = cleaned_data['name']
        # source_url_cleaned = cleaned_data['source_url']

        if all_sources.filter(name=name_cleaned).exists():
            self.add_error(None, ValueError('Name already exists!'))
        elif all_sources.filter(name=name_cleaned).exists():
            self.add_error(None, ValueError('Url already exists!'))


class RateForm(forms.ModelForm):

    class Meta:

        model = Rate
        fields = ('sale', 'buy', 'source', 'currency')


class ContactUsForm(forms.ModelForm):

    class Meta:

        model = ContactUs
        fields = ('email_from', 'subject', 'message')
