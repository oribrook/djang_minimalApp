from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response

from django.conf import settings

STATIC_PATH = str(settings.BASE_DIR) + r"\\my_app\\static\\"



def home(request):
    return HttpResponse("<h1> Welcome to Django minimal APP for loading File </h1>")


@api_view(['POST'])
def save_file(request):
        
    # new_file_name = request.data.get("file").name
    new_file_name = """X:\\programming\\react\\ttd\\""" + request.data.get("file").name
    print(new_file_name)

    # with open(STATIC_PATH + new_file_name, 'wb+') as f:
    with open(new_file_name, 'wb+') as f:
        for chunk in request.data.get("file").chunks():
            f.write(chunk)

    return Response("File uploaded!")


@api_view(['POST'])
def save_files(request):
    
    dest_dir = """X:\\programming\\react\\ttd\\"""
    
    uploaded_files = request.FILES.getlist('files')
    for uf in uploaded_files:                
        with open(dest_dir + uf.name, 'wb+') as FH:
            for chunk in uf.chunks():
                FH.write(chunk)

    return Response("Files uploaded!")
