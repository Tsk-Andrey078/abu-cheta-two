from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Participant, ColichestvoDebilov
from .serializer import ParticipantSerializer, ColichestvoDebilovSerializer
from rest_framework.permissions import IsAuthenticated

class ParticipantsViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

class ColDebViewSet(viewsets.ModelViewSet):
    queryset = ColichestvoDebilov.objects.all()
    serializer_class = ColichestvoDebilovSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"