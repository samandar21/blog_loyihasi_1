from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class Articles(models.Model):
    title=models.CharField(max_length=200)
    summary=models.CharField(max_length=140,blank=True)
    body=RichTextField()
    photo=models.ImageField(upload_to='images/',blank=True)
    author=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})



class Comment(models.Model):
    article=models.ForeignKey(Articles,on_delete=models.CASCADE,related_name='comments')
    comment=models.CharField(max_length=150)
    author=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
        
    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("article_list")