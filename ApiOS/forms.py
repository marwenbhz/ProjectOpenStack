from django import forms

class SingUpForm(forms.Form):
    name=forms.CharField(250)
    tenant=forms.CharField(250)
    password=forms.CharField(widget=forms.PasswordInput)
