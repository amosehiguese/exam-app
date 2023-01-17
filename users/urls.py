from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.SignUpForm.as_view(), name='sign-up')
]
