from django.db import models
from core.models import Choice, Question, Survey


class Vote(models.Model):
    user = models.IntegerField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ManyToManyField(Choice, blank=True)
    text_answer = models.CharField(max_length=254, blank=True)


    def __str__(self):
        choice = self.choice.all()
        if self.question.qtype != 'text':
            return f'User {self.user} voted {self.question} with {choice}'
        return f'User {self.user} voted on {self.survey} in {self.question} with {self.text_answer}'

