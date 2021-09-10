from datetime import date
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models import Survey, Question, Choice
from core.serializers import SurveySerializer, QuestionSerializer, ChoiceSerializer


class SurveyViewSet(viewsets.ViewSet):
    """
    API endpoint that allows Surveys to be managed
    """
    permission_classes = [permissions.IsAuthenticated]


    def list(self, request):
        queryset = Survey.objects.all()
        serializer = SurveySerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk):
        survey = get_object_or_404(Survey.objects.all(), id=pk)
        serializer = SurveySerializer(survey)
        return Response(serializer.data)


    def create(self, request):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'OK', 'survey_id': serializer.data['id']})
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
            serializer.update(survey, data)
            return Response({'status': 'OK'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        survey = get_object_or_404(Survey.objects.all(), id=pk)
        survey.delete()
        return Response({'status': 'OK'})


    @action(detail=True,
            permission_classes=[AllowAny],
            url_path='questions')
    def questions(self, request, pk=None):
        survey = get_object_or_404(Survey.objects.all(), id=pk)
        questions = Question.objects.filter(survey=survey)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


    @action(detail=False,
            permission_classes=[AllowAny],
            url_path='active')
    def active_surveys(self, request):
        today = date.today()
        queryset = Survey.objects.filter(end_date__gte=today)
        serializer = SurveySerializer(queryset, many=True)
        return Response(serializer.data)


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Questions to be managed
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


    @action(detail=True,
            permission_classes=[AllowAny],
            url_path='choices')
    def choices(self, request, pk=None):
        question = get_object_or_404(Question.objects.all(), id=pk)
        choices = Choice.objects.filter(question=question)
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)


class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Choices to be viewed.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


    def create(self, request):
        question_id = request.data['question']
        if Question.objects.get(id=question_id).qtype == 'text':
            return Response({'status':'Questions with type TEXT can\'t have choices'})
        return super().create(request)
