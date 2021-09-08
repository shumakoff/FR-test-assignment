import factory
from core.models import Choice, Question, Survey
from voting.models import Vote


class SurveyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Survey


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question


class ChoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Choice


class VoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vote
