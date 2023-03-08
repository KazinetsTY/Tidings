from django.db import models


class News(models.Model):
    topic = models.CharField(max_length=100, blank=True)
    header = models.CharField(max_length=100)
    article = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
