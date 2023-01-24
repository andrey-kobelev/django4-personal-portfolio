from django.db import models


class AllBlogs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    date = models.DateField()
