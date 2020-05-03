from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Game(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.TextField()
    tags = models.TextField()
    developers = models.TextField()
    publishers = models.TextField()
    platforms = models.TextField()
    places_to_purchase = models.TextField()

    class Meta:
      verbose_name_plural = "games"

    def __str__(self):
        return self.title


class Recommendation(models.Model):
    
    recommendation = models.TextField()

    class Meta:
          verbose_name_plural = "recommendations"

    def __str__(self):
        return self.recommendation


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})




#Reminder: add more fields