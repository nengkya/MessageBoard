from django.db import models

#create your models here
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
