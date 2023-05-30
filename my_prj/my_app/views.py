from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


def home(request):
    return HttpResponse("""
<h1> Welcome to Django minimal APP  <br/><br/> Class view example by form </h1>
<a href='http://127.0.0.1:8000/class'> Press here to load form </a>

""")


class MyClassView(View):

    def get(self, request):
        return render(request=request, template_name="my_app/form.html")
    
    def post(self, request):
        args = request.POST.get("name")        
        return HttpResponse(f"I'v got the following name: {args}")    
