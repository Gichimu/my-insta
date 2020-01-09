from django import forms
from .models import Image, Profile
from pyuploadcare.dj.models import ImageField

class editForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'bio']


class createForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'image_name', 'image_caption']

        
