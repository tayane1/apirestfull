from rest_framework import serializers
from api.models.forum import Forum


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'