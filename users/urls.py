from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('sign-up/', views.SignUpForm.as_view(), name='sign-up'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]
