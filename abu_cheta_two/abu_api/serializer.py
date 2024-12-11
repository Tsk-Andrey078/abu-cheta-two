from rest_framework import serializers
from .models import Participant, ColichestvoDebilov

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'full_name', 'place_of_study', 'teacher_full_name', 'teacher_phone', 'stage_one', 'stage_two']

class ColichestvoDebilovSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColichestvoDebilov
        fields = ['id', 'count']