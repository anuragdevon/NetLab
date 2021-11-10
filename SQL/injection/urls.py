from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.user_signup),
    path('login/', views.user_login),
]
