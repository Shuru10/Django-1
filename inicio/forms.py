from django import forms 

class PacienteFormularioBase(forms.Form):
    nombre = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=20)
    edad = forms.IntegerField()

class IngresarPacienteFormulario(PacienteFormularioBase):
    ...
    
class EditarPacienteFormulario(PacienteFormularioBase):
    ...
    

class BuscarPaciente(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)