# Imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import *

# Views
# User Add
@api_view(["POST"])
def user_signup_unsafe(request):
    try:
        inputData = request.data
        username = inputData["username"]
        password = inputData["password"]
        print(username, password)
        response = {"code": status.HTTP_200_OK, "message": "No Error"}
        try:
            # Check if user exists
            query = f"SELECT COUNT(username) FROM injection WHERE username = '{username}';"
            user_count = SQL_RunQuery(query, commit=False)[0][0]
            if(user_count >= 1):
                response = {"code": status.HTTP_409_CONFLICT, "message": "User already exists"}
            else:
                amount = 0
                # Add user
                query = f"INSERT INTO injection (username, password, amount) VALUES('{username}', '{password}', {amount});"
                print(query) 
                SQL_RunQuery(query, commit=True)
                print("done")
                response = {"code": status.HTTP_200_OK, "message": "User added!"}

            return Response(response)

        except Exception as e:
            response = {"code": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}
            return Response(response)

    except Exception as e:
        return Response(str(e), status.HTTP_400_BAD_REQUEST)

# User Login 
@api_view(["POST"])
def user_login_unsafe(request):
    try:
        inputData = request.data
        username = inputData["username"]
        password = inputData["password"]
        response = {"code": status.HTTP_200_OK, "message": "No Error"}
        try:
            # Check if username exists
            query = f"SELECT COUNT(username) FROM injection WHERE username = '{username}';"
            user_count = SQL_RunQuery(query=query, commit=False)[0][0]
            if(user_count == 1):
                # Check if password is correct
                query = f"SELECT * FROM injection WHERE password='{password}';"
                # query = "SELECT * FROM injection WHERE username='anurag' and password='unknown' or '1'='1';"
                user_data = SQL_RunQuery(query=query, commit=False)
                response = {"code": status.HTTP_200_OK, "message": f"{user_data}"}                  
            return Response(response)

        except Exception as e:
            response = {"code": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}
            return Response(response)

    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


# SQL injection Prevention
# User Add
@api_view(["POST"])
def user_signup_safe(request):
    try:
        # print("!!!!")
        inputData = request.data
        username = inputData["username"]
        password = inputData["password"]
        response = {"code": status.HTTP_200_OK, "message": "No Error"}
        try:
            # Check if user exists
            query = f"SELECT COUNT(username) FROM injection WHERE username = '{username}';"
            user_count = SQL_RunQuery(query, commit=False)[0][0]
            if(user_count == 1):
                response = {"code": status.HTTP_409_CONFLICT, "message": "User already exists"}
            else:
                amount = 0
                # Make Password Hash
                password_hash = make_password_hash(password)
                # Add user
                print("!")
                print("Password:", password_hash)
                query = f"INSERT INTO injection (username, password, amount) VALUES('{username}', '{password_hash}', {amount});"
                SQL_RunQuery(query, commit=True)
                response = {"code": status.HTTP_200_OK, "message": "User added!"}

            return Response(response)

        except Exception as e:
            response = {"code": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}
            return Response(response)

    except Exception as e:
        return Response(str(e), status.HTTP_400_BAD_REQUEST)

# User Login 
@api_view(["POST"])
def user_login_safe(request):
    try:
        inputData = request.data
        username = inputData["username"]
        password = inputData["password"]
        response = {"code": status.HTTP_200_OK, "message": "No Error"}
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
                print(user_data)
                if user_data == []:
                    response = {"code": status.HTTP_401_UNAUTHORIZED, "message": "Invalid Password entered!"} 
                else:
                    response = {"code": status.HTTP_200_OK, "message": f"{user_data}"} 
            return Response(response)

        except Exception as e:
            response = {"code": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}
            return Response(response)

    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)