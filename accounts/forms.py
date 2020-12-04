from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class UserCreateForm(UserCreationForm):
	username = forms.CharField(label="Nombre de usuario:", required=True)
	email = forms.EmailField(label="Correo electrónico:",required=True)
	password1 = forms.CharField(label="Contraseña:", required=True, widget=forms.PasswordInput)
	password2 = forms.CharField(label="Confirmar contraseña:", required=True, widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		
		def save(self, commit=True):
			user = super(UserCreateForm, self).save(commit=False)
			user.email = self.cleaned_data["email"]
			if commit:
				user.save()
			return user

class UserLoginForm(AuthenticationForm):
	username = forms.CharField(label="Nombre de usuario:", required=True)
	password = forms.CharField(label="Contraseña:", required=True, widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ("username", "password")