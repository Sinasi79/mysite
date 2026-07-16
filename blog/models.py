from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.title


    
class Post(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to='projects/',default='projects/default.jpg')
    status = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    published_date = models.DateTimeField(null = True)
    more_info = models.TextField()
    more_info_header = models.CharField(max_length = 255)
    counted_views = models.IntegerField(default = 0)
    category = models.ManyToManyField(Category)

    class Meta :
        ordering = ('created_date',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self) :
        return reverse('project',kwargs={'pid':self.id})
        


