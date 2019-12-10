from django import forms
from django.forms import ModelForm, Textarea

class InputForm(forms.ModelForm):  
    
    class Meta:
        model = Input
        fields = ("file",'description')
        widgets = {
            'description': Textarea(),
        }