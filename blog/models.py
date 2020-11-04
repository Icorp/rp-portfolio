from django.db import models

# Category ...
class Category(models.Model):
    name = models.CharField(max_length=20)

# Posts ...
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False)
    categories = models.ManyToManyField("Category",related_name='posts')
