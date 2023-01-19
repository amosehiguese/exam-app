from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='Enter at least 8 character', label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, help_text=None, label='Re-enter Password')
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean_email(self):
        pass