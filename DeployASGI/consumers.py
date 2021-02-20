import json 
from channels.generic.websocket import WebsocketConsumer

class MiSocketConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self):
        pass

    def receive(self,text_data):
        pass

    