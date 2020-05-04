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

    #REC SECTION-----------------------------------
    rec_1 = models.TextField()
    rec_2 = models.TextField()
    rec_3 = models.TextField()
    rec_4 = models.TextField()
    rec_5 = models.TextField()
    #----------------------------------------------

    class Meta:
      verbose_name_plural = "games"

    def __str__(self):
        return self.title

    def info_preview(self):
        return self.body
        



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