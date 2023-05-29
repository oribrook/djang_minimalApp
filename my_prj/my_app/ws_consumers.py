from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class MyConsumer(WebsocketConsumer):

    def connect(self):
        # accept connection
        self.accept() 
        
        # send message to client
        self.send(text_data=json.dumps({'message': "ws-connection established"}))        

        # add user to group
        self.group_name = 'global'
        async_to_sync(self.channel_layer.group_add)(
                self.group_name, 
                self.channel_name)    

    def receive(self, text_data):
        text_data = json.loads(text_data)        
        
        # send feedback only to the sender
        # self.send(text_data=json.dumps({'message': f"new message '{text_data}' received"}))

        # forward message to all
        async_to_sync(self.channel_layer.group_send)(
            self.group_name, {
                    'message': text_data['message'],
                    'type': 'global_handler',  # this is a function                    
                }
            )
    
    def global_handler(self, event):
        """ This function will be run by each channel """

        self.send(text_data=json.dumps(
            {'message': event['message']}))