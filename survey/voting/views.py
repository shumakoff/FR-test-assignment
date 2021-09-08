from datetime import date
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.models import Survey, Question, Choice
from voting.models import Vote
from voting.serializers import VoteSerializer


class VoteViewSet(viewsets.ViewSet):
    """
    API endpoint that allows Votes to be viewed.
    """


    def retrieve(self, request, pk):
        votes = Vote.objects.filter(user=pk)
        if votes.exists():
            serializer = VoteSerializer(votes, many=True)
            return Response(serializer.data)
        return Response({'status': 'User haven\'t voted yet'},
                        status.HTTP_404_NOT_FOUND)


    def create(self, request):
        user_id = request.data['user_id']
        question_id = request.data['question']
        choices = request.data['answer']
        question = get_object_or_404(Question.objects.all(), id=question_id)
        if question.survey.end_date < date.today():
                return Response({'status': 'The survey is closed'})
        if question.qtype != 'text':
            vote, created = Vote.objects.get_or_create(user=user_id,survey=question.survey,question=question)
            if not created:
                return Response({'status': 'You already voted'})
            for choice in choices:
                vote.choice.add(choice)
            return Response({'status': 'OK'})
        else:
            vote, created = Vote.objects.get_or_create(user=user_id,survey=question.survey,question=question)
            if not created:
                return Response({'status': 'You already voted'})
            vote.text_answer = choices
            vote.save()
            return Response({'status': 'OK'})
