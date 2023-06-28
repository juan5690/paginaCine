from django import forms
from .models import persona, pelicula

class personaForm(forms.ModelForm):
    
    class Meta:
        model=persona
        fields=["rut","nombre","apellido"]
        

class peliculaForm(forms.ModelForm):
    
    class Meta:
        model = pelicula
        fields = ["nombrePeli", "descripcion", "credYreparto", "portada", "linkTrailer"]
        
class frmUpdatePersona(forms.ModelForm):

    class Meta:
        model=persona
        fields=["nombre"]
        #fields=["nombre","apellido","sexo"]