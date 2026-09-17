from django.db import models
# Create your models here.

class Profile(models.Model):
    
    full_name = models.CharField(max_length=50)
    title = models.CharField(max_length= 100)
    profile_image = models.ImageField(upload_to= 'static/profile/')
    short_bio = models.CharField( max_length= 200)
    about = models.TextField()
    
    email = models.EmailField()
    phone = models.CharField( max_length= 20)
    location = models.CharField(max_length= 100)
    
    
    github = models.URLField( blank=True)
    facebook = models.URLField(blank=True)
    linkedln = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    
    
    
    resume = models.FileField(upload_to= 'media/static/resume/')
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.full_name