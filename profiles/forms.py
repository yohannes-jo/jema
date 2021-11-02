from django import forms
from sorl.thumbnail import fields

from .models import Profile

class ProfileRegistrationForm(forms.ModelForm):
    """Register a new user."""
    class Meta:
        model = Profile
        fields = ['name', 'email', 'picture', 'bio']

