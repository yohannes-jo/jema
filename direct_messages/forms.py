from django import forms
from django.db.models import fields

from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['reciever', 'text']