from django import forms
from .models import Contact




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # email_base, provider = email.split("@")
        # domain, extension = provider.split(".")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name
