from django.urls import path
from . import views

urlpatterns = [
    path('insecure/signup/', views.user_signup_unsafe),
    path('insecure/login/', views.user_login_unsafe),
    path('secure/signup/', views.user_signup_safe),
    path('secure/login/', views.user_login_safe),
]
