from rest_framework import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import JsonResponse

@api_view(['POST'])
def user_signin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username == 'admin' and password == 'admin':
        return Response({'token': '123456789'})
    return Response({'error': 'Wrong username or password'})

@api_view(['POST'])
def user_signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username == 'admin' and password == 'admin':
        return Response({'token': '123456789'})
    return Response({'error': 'Wrong username or password'})

@api_view(['POST'])
def user_get(request):
    token = request.data.get('token')
    if token == '123456789':
        return Response({'username': 'admin'})
    return Response({'error': 'Invalid token'})

@api_view(['POST'])
def user_update(request):
    token = request.data.get('token')
    if token == '123456789':
        return Response({'username': 'admin'})
    return Response({'error': 'Invalid token'})

@api_view(['POST'])
def user_logout(request):
    token = request.data.get('token')
    if token == '123456789':
        return Response({'username': 'admin'})
    return Response({'error': 'Invalid token'})