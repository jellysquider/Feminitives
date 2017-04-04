from django.contrib import admin

# Register your models here.
from .models import Word

class WordAdmin(admin.ModelAdmin):
    class Meta:
        model = Word


admin.site.register(Word, WordAdmin)
