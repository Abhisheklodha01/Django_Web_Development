from django import forms
from .models import ChaiVariety

class ChaiVarityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(), label="Select chai varity")
    