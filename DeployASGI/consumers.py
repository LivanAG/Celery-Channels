import json 
from channels.generic.websocket import AsyncWebsocketConsumer

class MiSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('hola',self.channel_name)
        await self.accept()

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard('hola',self.channel_name)
        print("se cayo esta talla")

    async def receive(self,text_data):
        data = json.loads(text_data)
        await self.send(text_data=json.dumps({ 'mensaje': "Funciona"}))

    async def actualizar(self,event):
        await self.send(text_data=json.dumps({ 'mensaje': "Funciona"}))

    