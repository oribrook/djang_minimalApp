import  rest_framework.pagination as pgn
from rest_framework import generics

from my_app.models import Note
from my_app.serializers import NoteSerializer


class MyPagination(pgn.PageNumberPagination):
   page_size = 10       # default page-size
   max_page_size = 100   # can't be override by param
   page_query_param = "page_num"
   page_size_query_param = "page_size"

   # http://127.0.0.1:8000/notes_pagination2?page_num=X&page_size=X
   

class NotePagination(generics.ListAPIView):
   queryset = Note.objects.all()
   serializer_class = NoteSerializer
   pagination_class = MyPagination
