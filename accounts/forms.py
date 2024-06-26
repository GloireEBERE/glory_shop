from typing import Any
from django import forms
from .models import Account, UserProfile

class Registrationform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Saisissez votre mot de passe',
        'class': 'form-control',
    }))
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmez votre mot de passe'
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
    
    def __init__(self, *args, **kwargs):
        super(Registrationform, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Entrez le prénom'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Entrez le nom'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Entrez le numéro de téléphone'
        self.fields['email'].widget.attrs['placeholder'] = 'Entrez l\'adresse e-mail'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    def clean(self):
        cleaned_data = super(Registrationform, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError(
                "Le mot de passe est incorrect."
            )


class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number')
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages= {'invalid':("Seulement le fichier image.")}, widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture')
    
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'