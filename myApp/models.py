from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
  owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="user_posts",
        
    )
  
  title = models.CharField(max_length=10000)
  content = models.TextField(max_length=100000)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  
class Comment(models.Model):
  author = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True, related_name="userComment")
  post = models.ForeignKey(Post,on_delete=models.CASCADE, blank=True, null=True, related_name="post")
  message = models.CharField(max_length=200)
  def __str__(self):
    return f"{self.author} comment on {self.post.title}"