from django import forms
from .models import Image, Profile
from pyuploadcare.dj.models import ImageField

class editForm(forms.ModelForm):
    photo = ImageField()
    bio = forms.CharField(label='bio', max_length=50)

    class Meta:
        model = Profile
        fields = ('photo', 'bio')
