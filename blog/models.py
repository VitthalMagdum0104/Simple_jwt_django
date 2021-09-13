from django.db import models
from django.db.models.base import Model
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    slug = models.SlugField(unique=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.title} by {self.created_by.username}"
