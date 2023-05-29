from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request=request, template_name='my_app/index.html')


