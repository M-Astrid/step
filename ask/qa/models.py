from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Question(models.Model):

    title = models.CharField(max_length=255)
    text = models.CharField(max_length=1000)
    added_at = models.DateField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='likes_set')

    def __str__(self):
        return self.title

    def get_url(self):
        return "/question/{}/".format(self.id)

class Answer(models.Model):

    text = models.CharField(max_length=1000)
    added_at = models.DateField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.text