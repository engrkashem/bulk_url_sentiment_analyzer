from django.db import models

# Create your models here.


class UrlSentimentModel(models.Model):
    url = models.URLField(null=True, blank=True)
    is_processed = models.BooleanField(default=False)
    sentiment = models.TextField(null=True, blank=True)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.url[:30]}'
