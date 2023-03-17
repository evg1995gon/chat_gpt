from django import forms
from .models import Pictures


class PictureForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = Pictures
