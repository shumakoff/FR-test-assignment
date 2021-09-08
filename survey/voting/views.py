from datetime import date
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.models import Survey, Question, Choice
from voting.models import Vote
from voting.serializers import VoteSerializer, VotingSerializer, VotingTextSerializer, VotingSelectSerializer


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
        serializer = VotingSerializer(data=request.data)
        # first we check fields user_id and question
        if serializer.is_valid():
            question_id = serializer.data['question']
            user_id = serializer.data['user_id']
            question = get_object_or_404(Question.objects.all(), id=question_id)
            if question.survey.end_date < date.today():
                    return Response({'status': 'The survey is closed'})
            if question.survey.start_date > date.today():
                    return Response({'status': 'The survey is not yet open'})

            if question.qtype != 'text':
                serializer = VotingSelectSerializer(data=request.data)
                # then we check answer field
                # since we need to figure out if answer is a char or an id
                if serializer.is_valid():
                    choices = serializer.data['answer']
                    vote, created = Vote.objects.get_or_create(user=user_id,survey=question.survey,question=question)
                    if not created:
                        return Response({'status': 'You already voted'})
                    for choice in choices:
                        choice = get_object_or_404(Choice.objects.filter(question=question), id=choice)
                        vote.choice.add(choice)
                    return Response({'status': 'OK'})
                else:
                    return Response(serializer.errors,
                                    status.HTTP_400_BAD_REQUEST)

            else:
                serializer = VotingTextSerializer(data=request.data)
                if serializer.is_valid():
                    choices = serializer.data['answer']
                    vote, created = Vote.objects.get_or_create(user=user_id,survey=question.survey,question=question)
                    if not created:
                        return Response({'status': 'You already voted'})
                    vote.text_answer = choices
                    vote.save()
                    return Response({'status': 'OK'})
                else:
                    return Response(serializer.errors,
                                    status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,
                            status.HTTP_400_BAD_REQUEST)

