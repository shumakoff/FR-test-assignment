# Generated by Django 2.2.10 on 2021-09-07 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20210907_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='text_answer',
            field=models.CharField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
