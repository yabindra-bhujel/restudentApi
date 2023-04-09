from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='menu/images')

    def __str__(self):
        return self.name


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='blog/images')

    def __str__(self):
        return self.title

    def get_username(self):
        return self.user.username


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.user.username
