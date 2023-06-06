from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import MyForm


def home(request):
    return HttpResponse("""
<h1> Welcome to Django minimal APP  - Forms </h1>
<a href='form'> Click here to fill form </a>
""")


def serve_form(request):
    if request.method == 'GET':
        return render(request=request, template_name="my_app/form_example.html", 
                      context={'form': MyForm(initial={'name': 'Ori'})})
    else:

        

        form = MyForm(data=request.POST)

        if form.is_valid():
            print("Yay")
            # todo: add to DB etc..
        else:
            # return bound form
            return render(request=request, template_name="my_app/form_example.html", 
                      context={'form': form})        