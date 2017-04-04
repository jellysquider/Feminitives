from django import forms

from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['masculinitive1', 'feminitive1', 'SYM1', 'link1']


    def valid_link(self):
        link1 = self.cleaned_data.get('link1')
        return link1
