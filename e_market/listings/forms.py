from django import forms
from .models import UserSearchedImage,ProductsReview

class SearchImageForm(forms.ModelForm):
    class Meta:
        model = UserSearchedImage
        fields = [
            'user',
            'searched_image'
        ]


class SubmitReviewForm(forms.ModelForm):
    class Meta:
        model = ProductsReview
        fields = [
            'user',
            'product',
            'review',
            'rating',
        ]

