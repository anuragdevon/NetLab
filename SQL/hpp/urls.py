from django.urls import path
from . import views

urlpatterns = [
    path('name/search/<str:username>/', views.user_get_money),
    path('insecure/login/addmoney/username=<str:username>/password=<str:password>/amount=<int:amount>/', views.user_add_money_secured),
    path('secure/login/token/username=<str:username>/password=<str:password>/amount=<int:amount>/', views.get_token),
    path('secure/login/transfer/username=<str:username>/amount=<int:amount>/receiver=<str:receiver>/token=<str:token>/', views.user_transfer_money),
]


