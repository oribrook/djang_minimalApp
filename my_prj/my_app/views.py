# from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import (api_view,
                             authentication_classes,
                             permission_classes)

from .models import Note
from .models import Note
from .serializers import NoteSerializer
from .paginators import MyPagination


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


@api_view(['POST'])
def signup(request):
    try:
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email", None)

        user = User.objects.create_user(username=username, password=password, email=email)

        token = Token.objects.create(user=user)
        token = token.key
    
        return Response({'msg': f"new user created. id: {user.id}", 'token': token})
    
    except Exception as e:
        print("\n\n***Error:", e, "\n\n")
        return Response("Server error.", 500)



@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def check_token(request):
    return Response({"msg": f"Token is valid.",
                     'user': request.user.username})



def home(request):
    return HttpResponse("<h1> Welcome to Django minimal APP </h1>")


@api_view(['GET'])
def serve_notes_pagination(request):
    page_size = int(request.GET.get("page_size", 20))
    page = int(request.GET.get("page_num", 0))

    start = page * page_size 
    end = start + page_size  
    
    notes = Note.objects.filter()[start:end]  # good!

    notes_data = NoteSerializer(notes, many=True).data    
    
    res = {'data': notes_data,           
           'has_more'  :  end <= Note.objects.count(),
           'total': Note.objects.count(),
           }

    return Response(res)
