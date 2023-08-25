from django import forms
from.models import signup, ImageModel


class signupForm(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'
    


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['title', 'image']

