# from django.shortcuts import render

from rest_framework import generics
from .serializer import ServerSerializer, ServerSerializerShort, PerfMonLogSerializer
from .models import Server, PerfMonLog


class PerfMonLogSet(generics.ListAPIView):
    queryset = PerfMonLog.objects.all()
    serializer_class = PerfMonLogSerializer


class PerfMonLogAddView(generics.CreateAPIView):

    queryset = PerfMonLog.objects.all()
    serializer_class = PerfMonLogSerializer


class PerfMonDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = PerfMonLog.objects.all()
    serializer_class = PerfMonLogSerializer


class ServerViewSet(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerAddView(generics.CreateAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerViewSetShort(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializerShort
