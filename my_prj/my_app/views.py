from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("""
    <h1> Welcome to Django minimal APP - branch: static-files </h1>
    <p> Here we are going to learn how to work with: <br/>
        A. Rendering data into html <br/>
        B. Django static files </p>
    <a href='http://127.0.0.1:8000/html'> link </a>
    """)


def serve_html(request):
    return render(request=request, template_name="index.html", 
           context={"title": "DMA",
                    "content": "This is a body content",
                    "some_list": [1,2,3]})


def serve_param(request, param):    
    return HttpResponse(f"param is: {param}")


def serve_extended_html(request):
    return render(request=request, template_name="extended.html", context={
        'title': 'DMA',
    })