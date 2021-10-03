from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    email = models.EmailField(max_length=255, unique=True)

    class Meta:
        ordering = ('username',)
    
    def __str__(self):
        return self.username
