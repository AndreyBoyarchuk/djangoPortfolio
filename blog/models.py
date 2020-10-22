from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250, blank=True)
    description = models.TextField()
    date = models.DateField()

# Create your models here.
