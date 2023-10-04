from django.contrib import admin
from .models import UrlSentimentModel
# Register your models here.

# admin.site.register(UrlSentimentModel)


@admin.register(UrlSentimentModel)
class UrlSentimentModelAdmin(admin.ModelAdmin):
    list_display = ['url', 'is_processed', 'sentiment', 'saved_at']
