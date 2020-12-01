from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(label='name', max_length=200)
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password')