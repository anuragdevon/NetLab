from django.urls import path
from . import views

urlpatterns = [
    path('name/<str:username>/', views.user_get_money_test),
    path('insecure/login/addmoney/username=<str:username>/password=<str:password>/amount=<int:amount>/', views.user_add_money_unsafe),
    path('insecure/login/transfer/username=<str:username>/amount=<int:amount>/receiver=<str:receiver>/', views.user_transfer_money_unsafe),
    path('secure/login/token/username=<str:username>/password=<str:password>/amount=<int:amount>/', views.get_token),
    path('secure/login/add/username=<str:username>/password=<str:password>/amount=<int:amount>/token=<str:token>/', views.user_add_money_safe),
    path('secure/login/transfer/username=<str:username>/amount=<int:amount>/receiver=<str:receiver>/token=<str:token>/', views.user_transfer_money_safe),
]
