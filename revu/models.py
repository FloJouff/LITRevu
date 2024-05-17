from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from authentication.models import User


from PIL import Image


class Ticket(models.Model):
    """Ticket model

    Args:
        models: django default model

    """
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    image = models.ImageField(blank=True, null=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    review_provided = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.headline}'

    IMAGE_MAX_SIZE = (600, 480)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            self.resize_image()


class Review(models.Model):
    """Review model

    Args:
        models: django default model

    """
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.headline}'


class UserFollows(models.Model):
    """Follower and following User model

    Args:
        models: django default model
    """
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name='followed_by')

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = (
            "user",
            "followed_user",
        )


class BlockedUser(models.Model):
    """Blocked User model

    Args:
        models: django default model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='blocked_users')
    blocked_user = models.ForeignKey(User, on_delete=models.CASCADE,
                                     related_name='blocked_by_users')

    class Meta:
        unique_together = (
            'user',
            'blocked_user'
        )
