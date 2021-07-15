from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Team(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    users = models.ManyToManyField(related_name='users')


class Project(models.Model):
    title = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='team')


class Activities(models.Model):
    item = models.CharField(max_length=200)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='project')
