from django.db import models
from django.contrib.auth.models import User


class URL(models.Model):
    link_full = models.URLField(max_length=500, unique=True)
    link_short = models.CharField(max_length=150, unique=True)
    clicks_quantity = models.IntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    time_create = models.DateTimeField(auto_now_add=True)