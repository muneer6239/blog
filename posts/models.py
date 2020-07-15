from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, help_text="Please enter title below 50 char", unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, default=1)
    head0 = models.CharField(max_length=200, verbose_name="Header")
    chead0 = models.CharField(max_length=5000, verbose_name="Content of header")
    head1 = models.CharField(max_length=500, verbose_name=" Sub header")
    chead1 = models.TextField(verbose_name="Content of sub header")
    about = models.CharField(max_length=500, verbose_name="About post", default="Add something about post")
    pub_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images')
    read = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    