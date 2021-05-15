from django.db import models
from django.db.models import Model, CharField, TextField, BooleanField, DateTimeField
from django.contrib.auth.models import User

import time
from time import strftime


# Create your models here.
class Post(Model):

    title = CharField(max_length=100)
    city = CharField(max_length=100)
    body = TextField(max_length=500)
    img = CharField(max_length=600)
    create_at = DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create_at']
