from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_creator = models.BooleanField(default=True)

    def __str__(self):
        return self.username


