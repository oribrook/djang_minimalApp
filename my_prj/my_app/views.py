from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response

from django.conf import settings

STATIC_PATH = str(settings.BASE_DIR) + r"\\my_app\\static\\"



def home(request):
    return HttpResponse("<h1> Welcome to Django minimal APP </h1>")


@api_view(['POST'])
def save_file(request):
    
    print(request.data)

    new_file_name = f"my_file.PNG"    
    with open(STATIC_PATH + new_file_name, 'wb+') as f:
        for chunk in request.data.get("img").chunks():
            f.write(chunk)

    return Response("File uploaded!")
