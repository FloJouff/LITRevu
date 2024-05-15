from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    DEVELOPER = "DEVELOPER"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = (
        (DEVELOPER, 'Développeur'),
        (SUBSCRIBER, 'Utilisateur'),
    )

    profile_photo = models.ImageField(blank=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='suit',
    )
    # blocked_users = models.ManyToManyField(
    #     'self',
    #     blank=True,
    #     symmetrical=False,
    #     verbose_name='blocked_by',
    # )

    def __str__(self):
        return f'{self.username}'
