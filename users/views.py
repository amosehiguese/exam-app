from django.shortcuts import render, redirect
from django.views import View
from .models import User
from .forms import UserRegistrationForm, PhoneNumberVerificationForm, PhoneNumberVerificationCodeForm

class SignUpForm(View):
    form_class = UserRegistrationForm
    initial = {'key':'value'}
    template_name = 'users/sign_up.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

class Verify_Phone_Number(View):
    form_class = PhoneNumberVerificationForm
    initial = {'key':'value'}
    template_name = 'users/verify_phone_number.html'
    def get(self, request, *args, **kwargs):
        pass
    
    def post(self, request, *args, **kwargs):
        pass