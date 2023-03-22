from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=1200, verbose_name="Статья")
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="child",
        blank=True, null=True
    )
