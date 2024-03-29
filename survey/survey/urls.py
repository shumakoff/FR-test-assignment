"""survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from core.views import SurveyViewSet, QuestionViewSet, ChoiceViewSet
from voting.views import VoteViewSet


router = routers.DefaultRouter()
router.register(r'surveys', SurveyViewSet, basename='surveyslist')
router.register(r'questions', QuestionViewSet, basename='questionslist')
router.register(r'choices', ChoiceViewSet, basename='choiceslist')
router.register(r'voting', VoteViewSet, basename='voteslist')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('api/v1/', include(router.urls))
]
