from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Ticket(models.Model):

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='images/')
    time_created = models.DateTimeField(auto_now_add=True)
    answered = models.BooleanField(default=False)


class Review(models.Model):

    RATING_0 = 0
    RATING_1 = 1
    RATING_2 = 2
    RATING_3 = 3
    RATING_4 = 4
    RATING_5 = 5

    RATINGS_OPTIONS = [
        (RATING_0, '- 0'),
        (RATING_1, '- 1'),
        (RATING_2, '- 2'),
        (RATING_3, '- 3'),
        (RATING_4, '- 4'),
        (RATING_5, '- 5')
    ]

    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)

    rating = models.PositiveSmallIntegerField(default='Unspecified', validators=[
        MinValueValidator(0),
        MaxValueValidator(5)],
        choices=RATINGS_OPTIONS,)

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        unique_together = ('user', 'followed_user')
