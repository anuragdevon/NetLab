from django.urls import path
from . import views

urlpatterns = [
    path('name/search/<str:username>', views.user_name),
]
