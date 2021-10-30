from django.db import models
from django.urls import reverse
from django.shortcuts import render

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE
    )
    slug = models.SlugField(max_length=50)
    summary = models.CharField(max_length=300)
    body = models.TextField()

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

