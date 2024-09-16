from rest_framework import viewsets
from api.models.sujet import Sujet
from api.serializers.sujet_serializer import SujetSerializer


class SujetViewSet(viewsets.ModelViewSet):
    queryset = Sujet.objects.all()
    serializer_class = SujetSerializer