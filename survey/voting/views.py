from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.models import Survey, Question, Choice
from core.serializers import SurveySerializer, QuestionSerializer, ChoiceSerializer
from voting.models import Vote
from voting.serializers import VoteSerializer


class VoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Votes to be viewed.
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
