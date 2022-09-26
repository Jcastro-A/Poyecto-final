from distutils.command.upload import upload
from django import forms
from django.forms import TextInput


class crearArticulo(forms.Form):
    titulo = forms.CharField(label="Titulo del artículo", max_length=100, required=True)
    creador = forms.CharField(label="Creador", required=True , max_length=40)
    fecha = forms.DateField(label="Fecha", widget=forms.TextInput(attrs={'placeholder': 'aaaa/mm/dd'})) #TODO Cambiar fecha manual a acutal
    contenido = forms.CharField(label="Contenido", required=True, max_length=3000, widget=forms.Textarea(attrs={'rows':'5', 'cols': '100'}))
