# from django.shortcuts import render
from django.http import HttpResponse

from my_app.models import Note
from my_app.serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.cache import cache


def home(request):
    return HttpResponse("""
    <h1> Welcome to Django minimal APP for: CACHE </h1> <br/> doc: <br/>
    <h3> all notes:  http://localhost:8000/notes </h2>
    <h3> with cache: http://localhost:8000/notes/cache </h2>
    <h3> create note: POST: http://localhost:8000/notes/cache  with {title: .. , content: ..}</h2>
    """)


@api_view(['GET'])
def serve_notes(request):
    notes = Note.objects.all()
    notes_data = NoteSerializer(notes, many=True).data
    return Response(notes_data)


@api_view(['GET'])
def serve_notes_cached(request):
        
    cache_notes = cache.get("notes")
    if cache_notes:
        print("Cache found. using it")
        return Response(cache_notes)
    
    print("Cache was not found. query db")
    notes = Note.objects.all()
    notes_data = NoteSerializer(notes, many=True).data

    cache.set("notes", notes_data)

    return Response(notes_data)


@api_view(['POST'])
def create_note(request):
    ns = NoteSerializer(data=request.data)
    if ns.is_valid():
        ns.save()
    else:
        pass
        # todo: deal with errors 

    cache.delete("notes")  # remove cache
    return Response("Added")
    


