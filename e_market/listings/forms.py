from django import forms
from .models import UserSearchedImage

class SearchImageForm(forms.ModelForm):
    class Meta:
        model = UserSearchedImage
        fields = [
            'searched_image'
        ]

        # widgets = {
        #     'searched_image': forms.ImageField(attrs={'class':'form-control'}),
        # }