from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('sign-up/', views.SignUpForm.as_view(), name='sign-up'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # password reset urls
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password-reset'),

    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password-reset-done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
]

