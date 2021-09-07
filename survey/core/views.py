from datetime import date
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.models import Survey, QuestionType, Question, Choice
from core.serializers import SurveySerializer, QuestionTypeSerializer, QuestionSerializer, ChoiceSerializer


class SurveyViewSet(viewsets.ViewSet):
    """
    API endpoint that allows Surveys to be managed
    """


    def list(self, request):
        queryset = Survey.objects.all()
        serializer = SurveySerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk):
        survey = get_object_or_404(Survey.objects.all(), id=pk)
        serializer = SurveySerializer(survey)
        return Response(serializer.data)


    def create(self, request):
        serializer = SurveySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        survey = get_object_or_404(Survey.objects.all(), id=pk)
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            # we can not change initial start date of survey
            data = serializer.validated_data
            new_date = data['start_date']
            if survey.start_date != new_date:
                return Response({'status': 'Changing start date is not allowed'})
            else:
                serializer.update(survey, data)
                return Response({'status': 'OK'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        survey = get_object_or_404(Survey.objects.all(), id=pk)
        survey.delete()
        return Response({'status': 'OK'})


class QuestionTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows QuestionTypes to be viewed.
    """
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Questions to be managed
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Choices to be viewed.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
