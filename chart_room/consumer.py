from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Message,user_bot
from trading_bot import zerodha_login
User = get_user_model()

from django.contrib.auth.models import auth, User
from trading_bot import chart_room_stocklink
#from .chatbot_2 import chatbot_response

class ChatConsumer(WebsocketConsumer):
    def fetch_messages(self, data):
        messages = Message.last_5_messages()
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def new_message(self, data):
        author = data['from']

        try:
            user_bot.objects.filter(user=author)[0]
        except:
            print("enception")
            user_bot.objects.create(
                user = author
            )

        answerbot = chart_room_stocklink.finding(data=data)
        #answerbot = chatbot_response(msg=str(data['message']))
        author_user = user_bot.objects.filter(user=author)[0]
        message = Message.objects.create(
            author=author_user,
            content=data['message'],
            answer = answerbot)
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'author': message.author.user,
            'content': message.content,
            'timestamp': str(message.timestamp),
            'answer':message.answer,

        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)


    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))