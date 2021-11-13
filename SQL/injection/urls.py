from django.urls import path
from . import views

urlpatterns = [
    path('insecure/signup/', views.insecure_user_signup),
    path('insecure/login/', views.insecure_user_login),
    path('secure/signup/', views.secure_user_signup),
    path('secure/login/', views.secure_user_login),
]
