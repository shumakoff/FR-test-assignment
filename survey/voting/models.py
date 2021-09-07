from django.db import models
from core.models import Choice, Question, Survey


class Vote(models.Model):
    user = models.IntegerField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ManyToManyField(Choice, blank=True)
    text_answer = models.CharField(max_length=254, blank=True)


    def __str__(self):
        return f'{user} voted on {survey} in {question} with {choice}'
