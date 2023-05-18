import  rest_framework.pagination as pgn
from rest_framework import generics

from my_app.models import Note
from my_app.serializers import NoteSerializer


class MyPagination(pgn.PageNumberPagination):
   page_size = 10
   page_query_param = "page_num"
   max_page_size = 100


class NotePagination(generics.ListAPIView):
   queryset = Note.objects.all()
   serializer_class = NoteSerializer
   pagination_class = MyPagination
