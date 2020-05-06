from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
import json
from .models import Feedback, Hospital


class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        fires when connect
        """
        self.hospital_id = self.scope['url_route']['kwargs']['pk']
        #self.feedback_group = 'feedbacks_%s' % self.hospital_id
        self.feedback_group = f'feedbacks_{self.hospital_id}'

        # Join feedback group - > to update on all together
        await self.channel_layer.group_add(
            self.feedback_group,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        """leave comments group"""
        await self.channel_layer.group_discard(
            self.feedback_group,
            self.channel_name
        )

    async def receive(self, text_data):
        """
        Fires when data is received from js
        """
        text_data_json = json.loads(text_data)
        text = text_data_json['text']
        hospital_id = text_data_json['hospital_id']
        await self.create_feedback(text, hospital_id)

        # Post comment to comment group
        await self.channel_layer.group_send(
            self.feedback_group,
            {
                'type': 'post_feedback',
                'text': text
            }
        )

    async def post_feedback(self, event):
        """
        callback function to a group
        """
        text = event['text']
        # Send message to WebSocket group
        await self.send(text_data=json.dumps({
            'text': text
        }))

    @database_sync_to_async
    def create_feedback(self, text, hospital_id):
        """
        Async function to create a Comment
        """
        if text:
            feedback = Feedback(text=text, hospital=Hospital.objects.get(id=hospital_id))
            feedback.save()
