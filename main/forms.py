from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        label="Nombre de usuario",
        required=True)

    password = forms.CharField(
        max_length=100,
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }),
    )


