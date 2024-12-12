from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Participant, ColichestvoDebilov
from .serializer import ParticipantSerializer, ColichestvoDebilovSerializer
from rest_framework.permissions import IsAuthenticated

class ParticipantsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    lookup_field = "id"

class ColDebViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ColichestvoDebilov.objects.all()
    serializer_class = ColichestvoDebilovSerializer
    lookup_field = "id"