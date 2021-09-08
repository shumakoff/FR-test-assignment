from datetime import date
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from core.models import Survey, Question, Choice


class SurveySerializer(serializers.ModelSerializer):
    """
    Survey serializer
    """
    class Meta:
        model = Survey
        fields = '__all__'


    def validate(self, data):
        """ Start of the survey must be
        < than end of the survey
        """
        start_date = data['start_date']
        end_date = data['end_date']
        if end_date <= start_date:
            raise serializers.ValidationError('end_date must be > than start_date')
        return data


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


class NewQuestionSerializer(serializers.ModelSerializer):
    """
    Serializer for creating Question and Choice
    within one request
    """
    qtype_id = 0
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['text', 'qtype_id', 'choices']

    def create(self, validated_data):
        print(validated_data)
        choices = validated_data.pop('choices')
        qtype = get_object_or_404(QuestionType.objects.all(), id=validated_data['qtype'])
        question = Question(survey_id=self.context['survey_id'],
                            qtype_id=qtype.id,
                            text=validated_data['text'])
        question.save()
        for choice_data in choices:
            choice_data['question_id'] = question.id
            Choice.objects.create(**choice_data)
        return question


