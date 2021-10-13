from django import forms
from remainderone.models import appuser
class profileupdate(forms.ModelForm):
    class Meta():
        model=appuser
        fields='__all__'
    
