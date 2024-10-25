from dataclasses import fields
from django import forms
from main.models import FeedBackCall


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBackCall
        fields = ["name", "phone_number"]

    name  = forms.CharField()
    phone_number = forms.CharField()
    
