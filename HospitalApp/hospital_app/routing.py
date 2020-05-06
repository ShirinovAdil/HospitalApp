from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    path('ws/details/<int:pk>', consumers.CommentConsumer),
]