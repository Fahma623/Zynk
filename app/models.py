from django.db import models

# Create your models here.

class Shop(models.Model):  
    name = models.CharField(max_length=255)  
    category = models.CharField(max_length=100, choices=[('Boutique', 'Boutique'), ('Bakery', 'Bakery'), ('Flower Shop', 'Flower Shop')])  
    location = models.CharField(max_length=255)  
    image = models.ImageField(upload_to='shop_images/')  
    description = models.TextField(blank=True)  
    link = models.URLField(blank=True)  

    def __str__(self):  
        return self.name  
