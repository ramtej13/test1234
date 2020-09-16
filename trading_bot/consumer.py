from channels.generic.websocket import AsyncWebsocketConsumer
import json
import time
import random
import asyncio



class DashConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.groupname = 'dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name
        )
        # print(self.scope)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )

    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        val = datapoint
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'youlogic',
                'value':val
            }
        )

    async def youlogic(self, event):#,closehist=closehist,openhist=openhist):
        other_val = event#['message']
        print(other_val)
        await self.send(text_data=json.dumps({'value':other_val,}))




