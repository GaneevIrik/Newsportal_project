from django import forms
from .models import Post


class PostF(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['author', 'title', 'text', 'rating']
