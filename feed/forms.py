from django import forms

from .models import Post, Comment, Share

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ['to']