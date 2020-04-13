"""Registration forms."""

# Django
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Models
#from django.contrib.auth.models import User
#from apps.registration.models import Profile
from apps.users.models import User
from apps.users.models import Profile


class UserCreationWithEmail(UserCreationForm):
    """User creation with email form."""

    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido.")
    first_name = forms.CharField(max_length=255, required=True, help_text="Requerido, 255 caracteres como máximo y debe ser válido.")
    last_name = forms.CharField(max_length=255, required=True, help_text="Requerido, 255 caracteres como máximo y debe ser válido.")   

    class Meta:
        """Meta class."""

        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado. Prueba con otro.")
        return email

class ProfileForm(forms.ModelForm):
    """Profile form."""

    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        try:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
        except User.DoesNotExist:
            pass

    def save(self, *args, **kwargs):
        super(ProfileForm, self).save(*args, **kwargs)
        self.instance.user.first_name = self.cleaned_data.get('first_name')
        self.instance.user.last_name = self.cleaned_data.get('last_name')
        self.instance.user.save()

        return self.instance

    class Meta:
        """Meta class."""

        model = Profile
        fields = ['picture', 'biography', 'website', 'first_name', 'last_name']
        widgets = {
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3', 'id': 'input_picture'}),
            'biography': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows':3, 'placeholder': 'Biografía', 'id': 'input_biography'}), 
            'website': forms.URLInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Página web', 'id': 'input_website'}),
        }

class EmailForm(forms.ModelForm):
    """Email model form."""
    
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido.")

    class Meta:
        """Meta class."""

        model = User
        fields = ("email", )

        def clean_email(self):
            email = self.cleaned_data.get("email")
            # Si el email es el dato que se cambió dentro de la lista de los campos del formulario modificados
            if 'email' in self.changed_data:
                if User.objects.filter(email=email).exists():
                    raise forms.ValidationError("El email ya está registrado. Prueba con otro.")
            return email
