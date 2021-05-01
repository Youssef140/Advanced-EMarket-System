from django import forms
from .models import UserSearchedImage

class SearchImageForm(forms.ModelForm):
    class Meta:
        model = UserSearchedImage
        fields = [
            'user',
            'searched_image'
        ]