# Imports
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import *

# Views
# UNSECURED-------------------------------------------------------------------------------------------------------------------------
# User Get Money
@api_view(["GET"])
def user_get_money(request, username):
    print(username)
    try:
        response = {"code": status.HTTP_200_OK, "message": "No Error"}
        try:
            response = {"code": status.HTTP_200_OK, "message": f"{username}"}        
            return Response(response)

        except Exception as e:
            response = {"code": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}
            return Response(response)

    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

# User Add Money HPP
@api_view(["GET"])
def user_add_money(request, username, password, amount):
    try:
        # inputData = request.data
        # password = inputData["password"]
        # amount = inputData["amount"]
        print(type(username), type(password), type(amount))
        username = str(username)
        password = str(password)
        response = {"code": status.HTTP_200_OK, "message": "No Error"}

        # User Authorization
        # Check if username exists
        try:
            query = f"SELECT COUNT(username) FROM injection WHERE username = '{username}';"
            user_count = SQL_RunQuery(query=query, commit=False)[0][0]
            if(user_count == 1):
                # Make Password Hash
                password_hash = make_password_hash(password)
                # Check if password is correct
                query = f"SELECT * FROM injection WHERE username='{username}' and password='{password_hash}'"
                user_data = SQL_RunQuery(query=query, commit=False)
                print(user_data)
                if user_data == []:
                    response = {"code": status.HTTP_401_UNAUTHORIZED, "message": "Invalid Password entered!"} 
                else:
                    query = f"UPDATE injection SET amount=amount+{amount} WHERE username = '{username}';"
                    SQL_RunQuery(query, commit=True)
                    response = {"code": status.HTTP_200_OK, "message": "Money added!"}
            else:
                response = {"code": status.HTTP_401_UNAUTHORIZED, "message": "Invalid Username entered!"}

            return Response(response)
        except Exception as e:
            response = {"code": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}
            return Response(response)

    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

# SECURED-------------------------------------------------------------------------------------------------------------------------
# User Transfer Money HPP
# Step 1: Get Token User
@api_view(["GET"])
def get_token(request, username, password, amount):
    try:
        amount = int(amount)
        response = {"code": status.HTTP_200_OK, "message": "No Error"}
        # User Authorization
        try:
            # Check if username exists
            query = f"SELECT COUNT(username) FROM injection WHERE username = '{username}';"
            user_count = SQL_RunQuery(query=query, commit=False)[0][0]
            if(user_count == 1):
                # Make Password Hash
                password_hash = make_password_hash(password)
                # Check if password is correct
                query = f"SELECT * FROM injection WHERE username='{username}' and password='{password_hash}'"
                user_data = SQL_RunQuery(query=query, commit=False)
                if user_data == []:
                    response = {"code": status.HTTP_401_UNAUTHORIZED, "message": "Invalid Password entered!"} 
                else:
                    print(type(amount))
                    token = token_generator(amount)
                    response = {"code": status.HTTP_200_OK, "message": f"Token Generated, Keep it safe!: {token}"}
            else:
                response = {"code": status.HTTP_401_UNAUTHORIZED, "message": "Invalid Username entered!"}

            return Response(response)
        except Exception as e:
            response = {"code": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}
            return Response(response)

    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

# Step 2 Transfer Money using valid tokem
@api_view(["GET"])
def user_transfer_money(request, username, amount, receiver, token):
    try:
        response = {"code": status.HTTP_200_OK, "message": "No Error"}
        try:
            amount = int(amount)
            # Check if token is valid
            regenerate_token = token_generator(amount)
            if(regenerate_token == token):
                # Check if user exists
                query = f"SELECT COUNT(username) FROM injection WHERE username = '{username}';"
                user_count = SQL_RunQuery(query, commit=False)[0][0]
                if(user_count == 1):
                    # Check if receiver exists
                    query = f"SELECT COUNT(username) FROM injection WHERE username = '{receiver}';"
                    receiver_count = SQL_RunQuery(query, commit=False)[0][0]
                    if(receiver_count == 1):
                        # Check if user has enough money
                        query = f"SELECT amount FROM injection WHERE username = '{username}';"
                        user_money = SQL_RunQuery(query, commit=False)[0][0]
                        if(user_money >= amount):
                            # Transfer money
                            query = f"UPDATE injection SET amount=amount-{amount} WHERE username = '{username}';"
                            print(query) 
                            SQL_RunQuery(query, commit=True)
                            print("done")
                            query = f"UPDATE injection SET amount=amount+{amount} WHERE username = '{receiver}';"
                            print(query) 
                            SQL_RunQuery(query, commit=True)
                            print("done")
                            response = {"code": status.HTTP_200_OK, "message": "Money transferred!"}
                        else:
                            response = {"code": status.HTTP_406_NOT_ACCEPTABLE, "message": "Not enough money"}
                    else:
                        response = {"code": status.HTTP_204_NO_CONTENT, "message": "Invalid receiver"}
                else:
                    response = {"code": status.HTTP_204_NO_CONTENT, "message": "Invalid username"}
            else:
                response = {"code": status.HTTP_401_UNAUTHORIZED, "message": "Invalid token"}

            return Response(response)
        
        except Exception as e:
            response = {"code": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}
            return Response(response)
    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
# SECURED-------------------------------------------------------------------------------------------------------------------------
# http://127.0.0.1:8000/secure/login/transfer/username=apurba/amount=500/reciever=anurag/token=5a01cf6100aa9768ebae267414b29177b5ed5179fae498d33d223d65a3b1edf5/

# http://127.0.0.1:8000/insecure/login/addmoney/username=<str:nitish>/password=<str:1234>/amount=<str:1000>/
# insecure/login/addmoney/nitish/1234/1000/
# insecure/login/addmoney/username=apurba/password=789/amount=1000/
# {
#     "username": "nitish",
#     "password": "123",
#     "amount": 1000
# }

# {
#     "username": "anurag",
#     "password": "456",
#     "amount": 5000
# }

# SECURED-------------------------------------------------------------------------------------------------------------------------
# User Add Money HPP
@api_view(["GET"])
def user_add_money_secured(request, username, password, amount, token):
    try:
        inputData = request.data
        # password = inputData["password"]
        # amount = inputData["amount"]
        print(type(username), type(password), type(amount))
        username = str(username)
        password = str(password)
        response = {"code": status.HTTP_200_OK, "message": "No Error"}

        # User Authorization
        # Check if username exists
        try:
            query = f"SELECT COUNT(username) FROM injection WHERE username = '{username}';"
            user_count = SQL_RunQuery(query=query, commit=False)[0][0]
            if(user_count == 1):
                # Make Password Hash
                password_hash = make_password_hash(password)
                # Check if password is correct
                query = f"SELECT * FROM injection WHERE username='{username}' and password='{password_hash}'"
                user_data = SQL_RunQuery(query=query, commit=False)
                print(user_data)
                if user_data == []:
                    response = {"code": status.HTTP_401_UNAUTHORIZED, "message": "Invalid Password entered!"} 
                else:
                    query = f"UPDATE injection SET amount=amount+{amount} WHERE username = '{username}';"
                    SQL_RunQuery(query, commit=True)
                    response = {"code": status.HTTP_200_OK, "message": "Money added!"}
            else:
                response = {"code": status.HTTP_401_UNAUTHORIZED, "message": "Invalid Username entered!"}

            return Response(response)
        except Exception as e:
            response = {"code": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}
            return Response(response)

    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)