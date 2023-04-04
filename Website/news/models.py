from django.db import models


class DeletedNews(models.Model):
    deleted_at = models.DateTimeField(auto_now_add=True, verbose_name="Удалено")
    header = models.CharField(max_length=100, blank=True, verbose_name="Заглавие статьи")
    article = models.TextField(blank=True, verbose_name="Статья")


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
    is_draft = models.BooleanField(default=False, verbose_name="Черновик")

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return f"/news/{self.section}/{self.pk}/"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.header.exists():
            self.is_draft = True
            super().save(force_update=True, *args, **kwargs)

    def delete(self, *args, **kwargs):
        DeletedNews.objects.create(
            header=self.header,
            article=self.article
        )
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]
        get_latest_by = "created_at"
