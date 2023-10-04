from django.urls import path
# from .views import index
from . import views

urlpatterns = [
    path('', views.url_sentiment_view, name='index'),
    # path('', views.UrlSentimetView.as_view(), name='index'),
]
