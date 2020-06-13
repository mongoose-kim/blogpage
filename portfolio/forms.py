from django import forms
from .models import Pofol

class Pofol(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']