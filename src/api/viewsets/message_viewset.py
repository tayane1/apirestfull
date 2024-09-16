from rest_framework import viewsets
from api.models.message import Message
from api.serializers.message_serializer import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer