from cgitb import text
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Ticket(models.Model):
    
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='images/')
    time_created = models.DateTimeField(auto_now_add=True)


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
    
    # weird UML infos:
    # max_length will get ignore when used with PositiveSmallIntergerField
    rating = models.PositiveSmallIntegerField(max_length=1024, default='Unspecified', validators=[
        MinValueValidator(0),
        MaxValueValidator(5)],
        choices=RATINGS_OPTIONS,)

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
