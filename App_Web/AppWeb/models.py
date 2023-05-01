from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    detail = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', null=True, blank=True)

class Wallpaper(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='wallpaper', null=True, blank=True)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatar', null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.image}"