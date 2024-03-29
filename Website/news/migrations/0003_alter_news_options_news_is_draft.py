# Generated by Django 4.1.7 on 2023-03-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'get_latest_by': 'created_at', 'ordering': ['-created_at'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='is_draft',
            field=models.BooleanField(default=False, verbose_name='Черновик'),
        ),
    ]
