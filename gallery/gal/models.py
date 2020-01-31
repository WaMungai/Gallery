from django.db import models
import datetime as dt

# Create your models here.
    
class Category(models.Model):
    category_name=models.CharField(max_length=30)
    
class Location(models.Model):
    location_name=models.CharField(max_length=30)

class Image(models.Model):
    photo_image=models.ImageField(upload_to='images/')
    image_name=models.CharField(max_length=30)
    description=models.TextField(max_length=60)
    category=models.ForeignKey(Category)
    location=models.ForeignKey(Location)
    pub_date=models.DateTimeField(auto_now_add=True)
    
