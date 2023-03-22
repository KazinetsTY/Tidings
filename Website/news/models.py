from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=100, verbose_name="Раздел")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"




class News(models.Model):
    section = models.ForeignKey(Section, on_delete=models.PROTECT, verbose_name="Раздел", blank=True, null=True)
    header = models.CharField(max_length=100, blank=True, verbose_name="Заглавие статьи")
    article = models.TextField(blank=True, verbose_name="Статья")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]
