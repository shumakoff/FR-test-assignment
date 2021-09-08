from django.shortcuts import get_object_or_404
from rest_framework import serializers
from core.models import Question, Choice
from core.serializers import ChoiceSerializer, QuestionSerializer, SurveySerializer
from voting.models import Vote


class VoteSerializer(serializers.ModelSerializer):
    """
    Vote object serializer
    """
    choice = ChoiceSerializer(many=True)
    question = QuestionSerializer()
    survey = SurveySerializer()
    class Meta:
        model = Vote
        fields = '__all__'


class VotingSerializer(serializers.Serializer):
    """
    Serializer for voting
    """
    user_id = serializers.IntegerField()
    question = serializers.IntegerField()


class VotingSelectSerializer(VotingSerializer):
    """
    Serializer for voting on SELECT type of questions
    """
    answer = serializers.ListField(
            child=serializers.IntegerField())


    def validate(self, data):
        """
        Check if ID of choice we received is valid
        """
        choices = data['answer']
        question = Question.objects.get(id=data['question'])
        if question.qtype != 'select-multiple' and len(choices) > 1:
            raise serializers.ValidationError('This is a question with single choice')
        queryset = Choice.objects.filter(question_id=data['question'])
        for choice in choices:
            get_object_or_404(queryset, id=choice)
        return data


class VotingTextSerializer(VotingSerializer):
    """
    Serializer for voting on TEXT type of questions
    """
    answer = serializers.CharField()
