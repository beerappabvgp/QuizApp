# Generated by Django 4.2.2 on 2023-09-03 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_creator',
            field=models.BooleanField(),
        ),
    ]
