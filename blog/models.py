from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# one to one elaqesi quraq
class Author(models.Model):
    user=models.OneToOneField(User,on_delete= models.CASCADE)
    bio=models.TextField()
    def __str__(self):
        return self.user.username

class Tag(models.Model):
    title=models.CharField(max_length=10)
    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=20,unique=True)
    description = models.TextField(null=True, blank=True)
    content = models.TextField()
    show = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0)
    image = models.ImageField(null=True,blank=True)
    created = models.DateField(auto_now_add=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,blank=True)
    tags=models.ManyToManyField(Tag)
    def __str__(self):
        return self.title
    
class ArticleImage(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='article_images/')


 