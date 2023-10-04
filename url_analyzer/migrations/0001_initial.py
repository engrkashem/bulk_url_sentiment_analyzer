# Generated by Django 4.2.5 on 2023-10-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlSentimentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('is_processed', models.BooleanField(default=False)),
                ('sentiment', models.TextField(blank=True, null=True)),
                ('saved_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]