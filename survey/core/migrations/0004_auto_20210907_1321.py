# Generated by Django 2.2.10 on 2021-09-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210907_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qtype',
            field=models.CharField(choices=[('text', 'text (multiple line)'), ('select', 'select'), ('select-multiple', 'Select Multiple')], max_length=254),
        ),
        migrations.DeleteModel(
            name='QuestionType',
        ),
    ]
