# reservation/forms.py

from django import forms
from .models import User, Ticket

class BookingForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['train', 'no_of_passengers', 'status']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
