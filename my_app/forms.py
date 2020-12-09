from django import forms
from .models import Client

class PostForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'surname', 'otchestvo', 'address', 'phone_number',)
