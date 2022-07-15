from django.utils import timezone

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models, serializers

import datetime


# Create your views here.

class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """

    def get(self, request):
        """
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = models.Link.public.all()
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class RecentLinkView(APIView):
    """
    Returns a list of recently created active links
    """

    def get(self, request):
        """
        Invoked whenever a HTTP GET Request is made to this view
        """
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = models.Link.public.filter(created_date__gte=seven_days_ago)
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class PostListApi(generics.ListAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer


class PostCreateApi(generics.CreateAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer


class PostDetailApi(generics.RetrieveAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer


class PostUpdateApi(generics.UpdateAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer


class PostDeleteApi(generics.DestroyAPIView):
    queryset = models.Link.objects.filter(active=True)
    serializer_class = serializers.LinkSerializer
