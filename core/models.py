# aiproject/core/models.py
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class NewsPage(models.Model): #новости
    title = models.CharField(max_length=400)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

class InterestingPage(models.Model): #интересное
    title = models.CharField(max_length=400)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

class Event(models.Model): #события
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    registration_link = models.URLField(blank=True, null=True)
    content = RichTextUploadingField(default='Needs to be filled out')


    def __str__(self):
        return self.title

class TeamMember(models.Model): #команда
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team_photos/', null=True, blank=True)
    content = RichTextUploadingField(default='Need to download')

    def __str__(self):
        return self.name

class ImageSlider(models.Model): #слайдер изо
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='sliders/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200, db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True)
    content = RichTextUploadingField()
def __str__(self):
    return self.title

class Tag(models.Model):
    """
    Model representing a tag associated with a blog post
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
