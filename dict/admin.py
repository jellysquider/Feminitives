from django.contrib import admin

# Register your models here.

from .models import Contact
from .forms import ContactForm

class InterestedPeople(admin.ModelAdmin):
    form = ContactForm
    # list_display = ["__str__", "full_name", 'email', "message", "timestamp"]
    # class Meta:
    #     model = Contact

admin.site.register(Contact, InterestedPeople)
