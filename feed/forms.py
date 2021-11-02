from django import forms

from sorl.thumbnail import ImageField

from .models import Post 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']