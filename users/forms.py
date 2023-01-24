from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import PhoneNumber

from django.utils.translation import gettext_lazy as _

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='Enter at least 8 characters', label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, help_text=None, label='Re-enter Password')
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(_('A user with that email already exists.'))

class PhoneNumberVerificationForm(forms.Form):
    '''A simple form for the user to enter their phone number.'''
    phone_number = forms.CharField(max_length=20)

class PhoneNumberVerificationCodeForm(forms.Form):
    '''A form that includes a single field for the user to enter the verification code they received via SMS.'''
    verification_code = forms.CharField(max_length=6)

