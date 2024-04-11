# core/views.py
from django.shortcuts import render
from .models import NewsPage, InterestingPage, Event, BlogPost, TeamMember

def home(request):
    latest_news = NewsPage.objects.all().order_by('-published_date')[:5]
    latest_interesting = InterestingPage.objects.all().order_by('-created_at')[:5]
    latest_team = TeamMember.objects.all().order_by('name')[:5]
    latest_event = Event.objects.all().order_by('-date')[:5]
    latest_blog = BlogPost.objects.all().order_by('-published_date')[:5]

    context = {
        'latest_news': latest_news,
        'latest_interesting': latest_interesting,
        'latest_team': latest_team,
        'latest_event': latest_event,
        'latest_blog': latest_blog,
    }
    return render(request, 'core/home.html', context)

def news_page_view(request):
    return render(request, 'core/news.html')

def interesting_page_view(request):
    return render(request, 'core/interesting.html')

def team_member_view(request):
    return render(request, 'core/team.html')

def event_view(request):
    return render(request, 'core/event.html')

def blog_post_view(request):
    return render(request, 'core/blogpost.html')
