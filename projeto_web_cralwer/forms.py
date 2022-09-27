from django import forms
from django.forms import ModelForm
from .models import Artigo

class ArtigoForm(ModelForm):
    url = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'ex: https://github.com/'}))
    class Meta:
        model = Artigo
        fields = ['titulo', 'url'] 