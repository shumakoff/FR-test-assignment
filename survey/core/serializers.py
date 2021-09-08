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
