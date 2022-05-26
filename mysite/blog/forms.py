from django import forms
from django.forms import ModelForm
from .models import NewResponse


class ResponseForm(ModelForm):
    class Meta:
        model = NewResponse
        fields = ['firstname', 'lastname', 'subject']