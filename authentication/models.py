from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    DEVELOPER = "DEVELOPER"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = (
        (DEVELOPER, 'Développeur'),
        (SUBSCRIBER, 'Utilisateur'),
    )

    profile_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.username}'
