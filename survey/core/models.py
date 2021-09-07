from django.db import models
from django.utils.translation import gettext_lazy as _


class Survey(models.Model):
    name = models.CharField(max_length=254)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=254)


    def __str__(self):
        return f'{self.name}; {self.start_date} - {self.end_date}'


class Question(models.Model):
    TEXT = "text"
    SELECT = "select"
    SELECT_MULTIPLE = "select-multiple"

    QUESTION_TYPES = (
        (TEXT, _("text (multiple line)")),
        (SELECT, _("select")),
        (SELECT_MULTIPLE, _("Select Multiple")),
    )

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    qtype = models.CharField(choices=QUESTION_TYPES, max_length=254)
    text = models.CharField(max_length=254)

    def __str__(self):
        return f'{self.text} in {self.survey}'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=254, blank=True)


    def __str__(self):
        return f'{self.answer}'
