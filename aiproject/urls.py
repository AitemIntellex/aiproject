# aiproject/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('login/management/', admin.site.urls),
    path('', include('core.urls')),  # Измените эту строку
    path('ckeditor/', include('ckeditor_uploader.urls')),  # Добавьте этот маршрут
]
