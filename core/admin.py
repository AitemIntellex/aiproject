from django.contrib import admin
from django.contrib.auth.models import User
from .models import (
    NewsPage,
    InterestingPage,
    Event,
    BlogPost,
    ImageSlider,
    TeamMember
)

admin.site.register(NewsPage)
admin.site.register(InterestingPage)
admin.site.register(Event)
admin.site.register(BlogPost)
admin.site.register(ImageSlider)
admin.site.register(TeamMember)
