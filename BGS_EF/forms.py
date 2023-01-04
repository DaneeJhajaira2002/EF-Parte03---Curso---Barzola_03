from django import forms

class FormDocente(forms.Form):
    codigo = forms.CharField(
        label = "Codigo"
    )
    nombre = forms.CharField(
        label = "Nombre"
    )
    apellido_paterno = forms.CharField(
        label = "Apellido paterno"
    )
    apellido_materno = forms.CharField(
        label = "Apellido materno"
    )
    dni = forms.CharField(
        label = "DNI"
    )
    Fecha_nacimiento = forms.DateField(
        label = "Fecha de nacimiento"
    )
    estado = forms.CharField(
        label = "Estado"
    )
    
class FormCurso(forms.Form):
    codigo = forms.CharField(
        label = "Codigo"
    )
    nombre = forms.CharField(
        label = "Nombre"
    )
    horas = forms.CharField(
        label = "Horas"
    )
    creditos = forms.IntegerField(
        label = "Creditos"
    )
    estado = forms.CharField(
        label = "Estado"
    )
    
