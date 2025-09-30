from django import forms
#importacion de modelos
from .models import usuario, rol, nivel_educacion
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm

rol_educador= 'Educador'
rol_estudiante= 'Estudiante'

class RegistroBase(forms.ModelForm):
    # Campos que el formulario pedirá al usuario
    username= forms.CharField(max_length=150, label='Nombre de usuario')
    password= forms.CharField(widget=forms.PasswordInput, label='Contrasena')

    nivel_educacion_id= forms.ModelChoiceField(
        queryset=nivel_educacion.objects.all(),
        empty_label="Escoge un opcion",
        label="Nivel de educacion",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    class Meta:
        model = usuario
        fields =['username','password']
    
    def save(self, commit = True, user_role_name=None):
       #llamar al save del formulario para obtener el ususario
        user = super().save(commit=False)
        #toco hashear
        user.set_password(self.cleaned_data["password"])
        #se asigna el nvel de educacion
        user.nivel_educacion =self.cleaned_data["nivel_educacion_id"]

        if user_role_name:
            try:
                user_rol=rol.objects.get(nombre_rol=user_role_name)
                user.rol=user_rol
            except rol.DoesNotExist:
                pass      

        if commit:
            user.save()
        return user

class EducRegistro(RegistroBase):
    pass

class EstuRegistro(RegistroBase):
    fecha_nacimiento= forms.DateField(
        label="Fecha de Nacimiento",
        widget=forms.DateInput(attrs={'type':'date', 'class':'form-control'})
    )

    class Meta(RegistroBase.Meta):
        fields = RegistroBase.Meta.fields + ['fecha_nacimiento'] 
    
    def save(self, commit=True, user_role_name=None):
        user = super().save(commit=False, user_role_name=user_role_name)
        user.fecha_nacimiento = self.cleaned_data["fecha_nacimiento"]
        
        if commit:
            user.save()
        return user
