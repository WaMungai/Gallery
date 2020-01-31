from django.db import models
import datetime as dt

# Create your models here.
    
class Category(models.Model):
    category_name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.category_name
    
    def save_category(self):
        self.save()
        
    def get_category(self):
        return Category.select().where(Category.category_name==self)
     
    
class Location(models.Model):
    location_name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.location_name
    
    def save_location(self):
        self.save()
        
    def get_location(self):
        return Location.select().where(Location.location_name==self)

class Image(models.Model):
    photo_image=models.ImageField(upload_to='images/')
    image_name=models.CharField(max_length=30)
    description=models.TextField(max_length=60)
    category=models.ForeignKey(Category)
    location=models.ForeignKey(Location)
    pub_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
    
    