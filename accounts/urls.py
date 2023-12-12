from django.urls import path
from . import views

urlpatterns = [
    path('signupaccount/', views.sign_up_account,name='sign_up_account'),
]
