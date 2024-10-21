from django import forms
from .models import Agent, Inquiry

class AgentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['name', 'address', 'mobile_number', 'email', 'description']

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'mobile_number', 'whatsapp_number', 'email', 'property_type', 'property_category', 'location', 'square_yards', 'budget_range']
