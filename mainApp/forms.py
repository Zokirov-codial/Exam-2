from django import forms
from .models import *

class TalabaQidirishForm(forms.Form):
    ismi = forms.CharField(label='Talabaning ismi', max_length=100)

class YangiTalabaForm(forms.ModelForm):
    class Meta:
        model = Talaba
        fields = ['ism', 'yosh', 'kurs', 'talaba_id',]
class YangiRejaForm(forms.ModelForm):
    class Meta:
        model = Loyiha
        fields = ['sarlavha', 'sana', 'tafsilotlar', 'tugallangan', 'talaba', ]