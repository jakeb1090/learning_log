from django.db import models
from learning_logs.tmdb import MovieAPI
from urllib.parse import urlencode

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=299)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """return str representation of model"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else: 
            return self.text

class Poster(MovieAPI):
    def get_url(self):
        imgurl = m.imgurl(show=Topic)
        return urlencode(imgurl)
    