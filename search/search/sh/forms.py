from django import forms
from .models import Post
class Postmodel(forms.ModelForm):
    class Meta: 
        model = Post
        fields = [
            'title',
            'content'
        ]