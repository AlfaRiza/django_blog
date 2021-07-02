from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from tinymce.models import HTMLField


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    content = HTMLField()
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(null=True, blank=True)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', kwargs={
            'blog_id': self.id
        })

