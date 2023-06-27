from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def home(request):
    return HttpResponse("<h1> Welcome to DRF minimal APP </h1>")