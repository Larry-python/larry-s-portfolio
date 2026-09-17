from django.db import models
from my_profile.models import Profile
# Create your models here.
class Skill(models.Model):
 
    profile = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name = 'skills')
    name = models.CharField()
    percentage =models.PositiveIntegerField()
    icon = models.ImageField(upload_to= 'icon/')
    
    
    
    def __str__(self):
        return self.name
    
    
    
class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete= models.CASCADE,related_name='project')
    title = models.CharField(max_length=30)
    image= models.ImageField(upload_to='project-image')
    preview = models.URLField() #display a short video that show the preview of the project 
    link = models.URLField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    
    

class Service(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='services'
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(
        upload_to='services/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
    
    
    
class Testimonial(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='testimonials'
    )
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    image = models.ImageField(
        upload_to='testimonials/',
        blank=True,
        null=True
    )
    rating = models.PositiveIntegerField(default=5)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name