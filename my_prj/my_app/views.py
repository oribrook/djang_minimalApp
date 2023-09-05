from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("""
<h1> Welcome to Django App for Websocket </h1>
<h3> You can test the app by opening it from few different browser tabs. </h3> <br/>
<h4> powered by Logicode </h4>
<br/>
<a href='http://127.0.0.1:8000/chat'> Connect to our chat </a>
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


def send_to_rooms(req):
    from channels.layers import get_channel_layer    
    from asgiref.sync import async_to_sync

    room = req.GET.get("room", "room_global")
    msg = req.GET.get("msg", "example message by view")

    channel_layer = get_channel_layer()
        
    async_to_sync(channel_layer.group_send)(room, {
           'type': 'global.handler',
           'message': msg,
           'event_type': 'routine',
        })
    
    return HttpResponse(str(list(channel_layer.groups.keys())))
