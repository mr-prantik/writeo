from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id} \n Title: {self.title}\n Content: {self.content}"
    
    def get_absolute_url(self):
        return reverse('main:post-detail', kwargs={'pk':self.pk})