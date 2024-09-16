from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .viewsets.forum_viewset import ForumViewSet
from .viewsets.message_viewset import MessageViewSet
from .viewsets.sujet_viewset import SujetViewSet

router = routers.DefaultRouter()
router.register(r'forum', ForumViewSet)
router.register(r'message', MessageViewSet)
router.register(r'sujet', SujetViewSet)





urlpatterns = [
    path('', include(router.urls)),
]