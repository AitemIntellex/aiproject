from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db.models import ManyToManyField

from .models import (
    NewsPage,
    InterestingPage,
    Event,
    BlogPost,
    ImageSlider,
    TeamMember,
    Tag
)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date']
    search_fields = ['title', 'content']
    formfield_overrides = {
        ManyToManyField: {'widget': FilteredSelectMultiple("Tags", is_stacked=False)},
    }
    class Media:
        css = {
            'all': ('foundation/css/admin_custom.css',)  # Укажите путь к вашему CSS файлу
        }

# Регистрация моделей
admin.site.register(NewsPage)
admin.site.register(InterestingPage)
admin.site.register(Event)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(ImageSlider)
admin.site.register(TeamMember)
admin.site.register(Tag)
