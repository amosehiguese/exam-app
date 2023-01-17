from django.shortcuts import render, redirect
from django.views import View
from .models import User
from .forms import UserRegistrationForm

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