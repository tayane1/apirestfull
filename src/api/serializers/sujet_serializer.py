from rest_framework import serializers
from api.models.sujet import Sujet


class SujetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sujet
        fields = '__all__'