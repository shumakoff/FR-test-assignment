from datetime import date, timedelta
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APISimpleTestCase, APITransactionTestCase
from rest_framework.test import APIRequestFactory
from core.models import Choice, Question, Survey
from core.views import ChoiceViewSet, QuestionViewSet, SurveyViewSet
from voting.models import Vote
from voting.views import VoteViewSet
from .factories import SurveyFactory, QuestionFactory, ChoiceFactory, VoteFactory


class TestCaseForSurvey(APITestCase):


    def setUp(self):
        self.user = User.objects.create_user(
            username='user@foo.com', email='user@foo.com', password='top_secret')
        self.token = Token.objects.create(user=self.user)


    def test_create_survey_request_factory(self):
        request_factory = APIRequestFactory()
        request = request_factory.post(
                path='/api/v1/surveys/',
                data={'name': 'Test survey',
                'start_date':date.today(),
                'end_date':date.today()+timedelta(days=1),
                'description':'test_survey'},
                HTTP_AUTHORIZATION='Token {}'.format(self.token),
                format='json')
        survey_view = SurveyViewSet.as_view({'post':'create'})
        response = survey_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_question_request_factory(self):
        request_factory = APIRequestFactory()
        survey = Survey(name='test',
                        start_date=date.today(),
                        end_date=date.today()+timedelta(days=1),
                        description='test')
        survey.save()
        request = request_factory.post(
                path='/api/v1/questions/',
                data={'text': 'Test question',
                'survey':survey.id,
                'qtype':'text'},
                HTTP_AUTHORIZATION='Token {}'.format(self.token),
                format='json')
        question_view = QuestionViewSet.as_view({'post':'create'})
        response = question_view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
