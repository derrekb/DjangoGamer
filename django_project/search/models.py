from django.db import models

class Post(models.Model):
    title= models.CharField(max_length=300)
    slug= models.SlugField(max_length=300, unique=True, blank=True)
    content= models.TextField()
    pub_date = models.DateTimeField(auto_now_add= True)
    


    def __str__(self):
        return self.title

