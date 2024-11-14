from django import forms

from .models import Theme, Individual_Post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['name']
        labels = {'name':''}

class PostForm(forms.ModelForm):
    class Meta:
        model = Individual_Post
        fields = ['theme', 'text']
        labels = {'theme': '', 'text': ''}