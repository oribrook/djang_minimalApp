from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .models import Site
from .serializers import SiteSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def list(self, *args, **kwargs):
        print("About to run list")
        return super().list(*args, **kwargs)


def home(request):
    return HttpResponse("<h1> Welcome to Django minimal APP </h1>")


