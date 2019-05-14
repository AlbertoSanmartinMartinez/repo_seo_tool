#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# General Forms
class LoginForm(AuthenticationForm):
    """
    """

    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': u'Nombre de Usuario'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': u'Contraseña'}))


class ResetForm(forms.Form):
    """
    """
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Nombre de usuario o correo electrónico'}))


class ResetPasswordForm(forms.Form):
    """
    """

    username = forms.CharField(label="", widget=forms.HiddenInput)
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': u'Contraseña'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': u'Confirmar contraseña'}))


class ConfirmationForm(forms.Form):
    """
    """

    ok = forms.IntegerField(widget=forms.HiddenInput(), initial=1, label='')
