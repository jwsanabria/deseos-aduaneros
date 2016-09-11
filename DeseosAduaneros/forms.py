from django import forms
from DeseosAduaneros.models import Deseo

class DeseoForm(forms.ModelForm):
    class Meta:
        model = Deseo

        fields = [
            'personaje',
            'deseo'
        ]
        labels = {
            'personaje' : 'Personaje',
            'deseo' : "Deseo"
        }
        widgets = {
            'personaje': forms.Select(attrs={'class':'form-control'}),
            'deseo': forms.Textarea(attrs={'class':'form-control'})
        }