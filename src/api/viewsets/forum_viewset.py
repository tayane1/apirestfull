from rest_framework import viewsets
from api.models.forum import Forum
from api.serializers.forum_serializer import ForumSerializer


class ForumViewSet(viewsets.ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer