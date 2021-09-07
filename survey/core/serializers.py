from datetime import date
from rest_framework import serializers
from core.models import Survey, QuestionType, Question, Choice


class SurveySerializer(serializers.ModelSerializer):
    """
    Survey serializer
    """
    class Meta:
        model = Survey
        fields = '__all__'


class QuestionTypeSerializer(serializers.ModelSerializer):
    """
    QuestionType serializer
    """
    class Meta:
        model = QuestionType
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    """
    Question serializer
    """
    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    """
    Choice serializer
    """
    class Meta:
        model = Choice
        fields = '__all__'
