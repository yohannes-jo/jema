from django import forms

from sorl.thumbnail import ImageField

from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['image', 'caption']