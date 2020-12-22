from django import forms
from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'middle_name', 'policy_number',)

class FundForm(forms.ModelForm):
    class Meta:
        model = Fund
        fields = ('balance', )

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('client', 'fund', 'insurance_amount', 'conditions',)

