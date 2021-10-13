from django import forms
from remainderone.models import Room
class roomform(forms.ModelForm):
    class Meta():
        model=Room
        fields='__all__'