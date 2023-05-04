# from django.shortcuts import render
from django.http import HttpResponse

from my_app.models import Note
from my_app.serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


def home(request):
    return HttpResponse("<h1> Welcome to Django minimal APP </h1>")


@api_view(['GET'])
def serve_notes(request):
    notes = Note.objects.all()
    notes_data = NoteSerializer(notes, many=True).data
    return Response(notes_data)


@api_view(['GET'])
def serve_notes_pagination(request):
    page_size = int(request.GET.get("page_size", 20))
    page = int(request.GET.get("page_num", 0))

    start = page * page_size 
    end = start + page_size  

    # notes = Note.objects.all()[start, end-1] # bad!
    # notes = Note.objects.filter(id__range=[start, end-1])  # ok
    notes = Note.objects.filter()[start:end]  # good!

    notes_data = NoteSerializer(notes, many=True).data    
    
    res = {'data': notes_data,           
           'has_more'  :  end <= Note.objects.count()
           }

    return Response(res)
