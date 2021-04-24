from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = SearchImage
        fields = ['user', 'search_image']