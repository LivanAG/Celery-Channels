from .celery import app
from datetime import datetime


@app.task
def revision():
    from channels.layers import get_channel_layer
    from asgiref.sync import async_to_sync
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("hola",{"type": "actualizar",})

    return "Todo Bien"
