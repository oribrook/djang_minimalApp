from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("""
<h1> Welcome to Django App for Websocket </h1>
<h3> You can test the app by opening it from few different browser tabs. </h3> <br/>
<h4> powered by Logicode </h4>
<br/>
<a href='/chat'> Connect to our chat </a>
""")



def chat(req):
    return render(request=req, template_name='my_app/index.html')


def serve_chat_rooms(req):
    from channels.layers import get_channel_layer
    channel_layer = get_channel_layer()
    groups = channel_layer.groups.keys()
    return HttpResponse(str(list(groups)))


def serve_room_participants(req, group):
    from channels.layers import get_channel_layer
    channel_layer = get_channel_layer()
    participants = channel_layer.groups.get(group, "")

    return HttpResponse(str(list(participants)))
