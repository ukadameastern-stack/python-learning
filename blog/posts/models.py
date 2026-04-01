from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=60)
    post_content = models.TextField()
    published_date = models.DateField(auto_now=True)
    post_auther = models.CharField(max_length=30)
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.post_title
    

class Comment(models.Model):
    comment_content = models.TextField()
    comment_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,   # ✅ allow temporarily
        blank=True
    )
    comment_date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.comment_author.username}: {self.comment_content[:20]}"
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name    
