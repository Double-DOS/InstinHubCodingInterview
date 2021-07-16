from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Team(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    users = models.ManyToManyField(User, related_name='users')

    def __str__(self):
        return self.title


class UserImage(models.Model):
    image = models.ImageField(upload_to='images/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Activity(models.Model):
    item = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.item

    class Meta:
        verbose_name_plural = 'Activities'


class Project(models.Model):
    title = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='team')
    activities = models.ManyToManyField(Activity, related_name='activties')

    def __str__(self) -> str:
        return self.title
