from django.db import models

# Create your models here.

    
class Question(models.Model):
    text = models.TextField()
    

    def __str__(self):
        return self.text
    

class Answer(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


    