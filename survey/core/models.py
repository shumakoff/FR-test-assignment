from django.db import models


class Survey(models.Model):
    name = models.CharField(max_length=254)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=254)


    def __str__(self):
        return f'{self.name}; {self.start_date} - {self.end_date}'


class QuestionType(models.Model):
    qtype = models.CharField(max_length=254)


    def __str__(self):
        return f'{self.qtype}'


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    qtype = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    text = models.CharField(max_length=254)

    def __str__(self):
        return f'{self.text} in {self.survey}'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=254)


