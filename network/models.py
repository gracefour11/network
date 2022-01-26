from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="userID")
    contents = models.CharField(max_length=280, default=None)
    created_dt = models.DateTimeField(default=datetime.datetime.now)

    def __str__ (self):
        return f"{self.id}: {self.contents} by {self.user_id} on {self.created_dt}"

