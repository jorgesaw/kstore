"""Registration views."""

# Django
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy

# Forms
from django import forms
from apps.registration.forms import (
    UserCreationWithEmail, 
    ProfileForm, 
    EmailForm
)
from django.contrib.messages.views import SuccessMessageMixin

# Models
#from apps.registration.models import Profile
from apps.users.models import Profile


class SignUpView(CreateView):
    """Sign up view."""
    
    form_class = UserCreationWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register' 

    def get_form(self, form_class=None):
        """
            Override in exec time.
        """
        form = super(SignUpView, self).get_form()
        # Modify at real time.
        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}
        ) 
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Direción de e-mail'}
        ) 
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Contraseña'}
        )
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Repetir contraseña'}
        )
        form.fields['first_name'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre'}

        )
        form.fields['last_name'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Apellido'}

        )

        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(SuccessMessageMixin, UpdateView):
    """Profile update view."""

    form_class = ProfileForm
    success_url = reverse_lazy('registration:profile')
    template_name = 'registration/profile_form.html'
    success_message = "Datos de perfil actualizados exitosamente."

    def get_object(self):
        # Recuperar el objeto que se va a editar.
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

@method_decorator(login_required, name='dispatch')
class EmailUpdate(SuccessMessageMixin, UpdateView):
    """Email update view."""

    form_class = EmailForm
    template_name = 'registration/profile_email_form.html'
    success_message = "Email actualizado exitosamente."

    def get_success_url(self):
        #from django.contrib import messages
        #messages.success(self.request, 'Email actualizado')
        return reverse_lazy('registration:profile') #+ '?change_email'

    def get_object(self):
        # Recuperar el objeto que se va a editar.
        return self.request.user

    def get_form(self, form_class=None):
        """
            Override in exec time.
        """
        form = super(EmailUpdate, self).get_form()
        # Modify at real time. 
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Direción de e-mail', 'id': 'inputEmail'}
        )
        return form
