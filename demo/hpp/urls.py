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

# 20c2e0c4d077b78166d0c15240fc2dd14624355b416a1623037de1369d36ca00
# 59ef1f30f92b3b3634e851088a8764a3713a6402d951a8acd3e61459793d3288