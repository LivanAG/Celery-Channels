import json 
from channels.generic.websocket import AsyncWebsocketConsumer

class MiSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self,close_code):
        print("se cayo esta talla")

    async def receive(self,text_data):
        data = json.loads(text_data)
        await self.send(text_data=json.dumps({ 'mensaje': "Funciona"}))


    