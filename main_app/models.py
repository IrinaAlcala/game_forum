from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

RATINGS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4,4),
    (5,5)
)



# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    publisher = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('games_detail', kwargs={ 'pk': self.id })


class Review(models.Model):
    date = models.DateField('Review Date')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    rating = models.IntegerField(choices=RATINGS, default=RATINGS[0][4])
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
         return f"{self.get_review_display()} on {self.date}"

    class Meta:
        ordering = ['-date']