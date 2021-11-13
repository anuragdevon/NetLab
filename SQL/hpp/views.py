# Imports
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import *

# Views
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
@api_view(["POST"])
def user_add_money(request, username):
    try:
        inputData = request.data
        amount = inputData["amount"]
        response = {"code": status.HTTP_200_OK, "message": "No Error"}
        try:
            # Check if user exists
            query = f"SELECT COUNT(username) FROM injection WHERE username = '{username}';"
            user_count = SQL_RunQuery(query, commit=False)[0][0]
            if(user_count == 1):
                # Add money to user
                query = f"UPDATE injection SET money=money+{amount} WHERE username = '{username}';"
                print(query) 
                SQL_RunQuery(query, commit=True)
                print("done")
                response = {"code": status.HTTP_200_OK, "message": "Money added!"}

            return Response(response)

        except Exception as e:
            response = {"code": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}
            return Response(response)

    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

# User Transfer Money HPP
@api_view(["POST"])
def user_transfer_money(request, username):
    try:
        inputData = request.data
        amount = inputData["amount"]
        receiver = inputData["receiver"]
        response = {"code": status.HTTP_200_OK, "message": "No Error"}
        try:
            # Check if user exists
            query = f"SELECT COUNT(username) FROM injection WHERE username = '{username}';"
            user_count = SQL_RunQuery(query, commit=False)[0][0]
            if(user_count == 1):
                # Check if receiver exists
                query = f"SELECT COUNT(username) FROM injection WHERE username = '{receiver}';"
                receiver_count = SQL_RunQuery(query, commit=False)[0][0]
                if(receiver_count == 1):
                    # Check if user has enough money
                    query = f"SELECT money FROM injection WHERE username = '{username}';"
                    user_money = SQL_RunQuery(query, commit=False)[0][0]
                    if(user_money >= amount):
                        # Transfer money
                        query = f"UPDATE injection SET money=money-{amount} WHERE username = '{username}';"
                        print(query) 
                        SQL_RunQuery(query, commit=True)
                        print("done")
                        query = f"UPDATE injection SET money=money+{amount} WHERE username = '{receiver}';"
                        print(query) 
                        SQL_RunQuery(query, commit=True)
                        print("done")
                        response = {"code": status.HTTP_200_OK, "message": "Money transferred!"}
                    else:
                        response = {"code": status.HTTP_401_UNAUTHORIZED, "message": "Not enough money"}
                else:
                    response = {"code": status.HTTP_204_NO_CONTENT, "message": "Invalid receiver"}
            else:
                response = {"code": status.HTTP_204_NO_CONTENT, "message": "Invalid username"}

            return Response(response)
        
        except Exception as e:
            response = {"code": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}
            return Response(response)
    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
