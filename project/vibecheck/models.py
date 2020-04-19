from django.db import models
from django.contrib.auth.models import User
from django.core.validators import int_list_validator


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50)
    avatar_url = models.TextField(default="/static/vibecheck/img/default-avatar.png")
    join_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True)
    birthday = models.DateField(null=True)
    location = models.CharField(max_length=150, null=True)
    spotify_uri = models.TextField(default="spotify:playlist:37i9dQZF1DWYBO1MoTDhZI")


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    multi_media = models.TextField(null=True)
    tags = models.TextField(null=True)
