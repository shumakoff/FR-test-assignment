from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.models import Survey, QuestionType, Question, Choice
from core.serializers import SurveySerializer, QuestionTypeSerializer, QuestionSerializer, ChoiceSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Surveys to be viewed.
    """
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class QuestionTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows QuestionTypes to be viewed.
    """
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Questions to be viewed.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Choices to be viewed.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
