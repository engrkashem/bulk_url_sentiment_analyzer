
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('url_analyzer.urls')),
    path('admin/', admin.site.urls),
]
