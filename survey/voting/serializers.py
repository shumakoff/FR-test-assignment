from datetime import date
from rest_framework import serializers
from core.models import Survey, Question, Choice
from core.serializers import ChoiceSerializer
from voting.models import Vote


class VoteSerializer(serializers.ModelSerializer):
    """
    Survey serializer
    """
    choice = ChoiceSerializer(many=True)
    class Meta:
        model = Vote
        fields = '__all__'
