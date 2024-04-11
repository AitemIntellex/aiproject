# core/urls.py
from django.urls import path
from .views import (
    home,
    news_page_view,
    interesting_page_view,
    team_member_view,
    event_view,
    blog_post_view
)

urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('news/', news_page_view, name='news'),  # Страница новостей
    path('interesting/', interesting_page_view, name='interesting'),  # Страница интересных фактов
    path('team/', team_member_view, name='team'),  # Страница команды
    path('events/', event_view, name='events'),  # Страница событий
    path('blog/', blog_post_view, name='blog')  # Страница блога
]
