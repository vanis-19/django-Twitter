from rest_framework import generics
from .serializers import TweetModelSerializer
from tweets.models import Tweet
from rest_framework import permissions
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view



class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    def get_queryset(self):
        return Tweet.objects.all()


class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TweetUpdateAPIView(generics.UpdateAPIView):

    serializer_class = TweetModelSerializer
    queryset = Tweet.objects.all()






