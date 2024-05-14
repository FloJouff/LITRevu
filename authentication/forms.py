from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class SignupForm(UserCreationForm):
    password1 = forms.CharField(label="Mot de passe",
                                strip=False,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'style': 'width: 300px'}),
                                help_text='',)
    password2 = forms.CharField(label="Confirmer votre mot de passe",
                                strip=False,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'style': 'width: 300px'}),
                                help_text='',)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'style': 'width: 300px',
                                               'label': 'Nom d\'utilisateur'},)
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d\'utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput,
                               label='Mot de passe')

    widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
