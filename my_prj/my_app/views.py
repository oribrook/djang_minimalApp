from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import (api_view,
                             authentication_classes,
                             permission_classes)
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(["GET", "POST"])
def home(request):
    return Response("Welcome to Django minimal APP")


@api_view(['POST'])
def signup(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email", None)

    user = User.objects.create_user(username=username, password=password, email=email)

    return Response(f"new user created. id: {user.id}")


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def private(request):
    return Response(f"This is a private response. user is: {request.user.username}")


@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def check_token(request):
    return Response({"msg": f"Token is valid.",
                     'user': request.user.username})
