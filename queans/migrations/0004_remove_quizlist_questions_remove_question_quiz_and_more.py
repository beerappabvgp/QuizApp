# Generated by Django 4.2.4 on 2023-09-04 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queans', '0003_alter_quizlist_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizlist',
            name='questions',
        ),
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='QuizList',
        ),
    ]
