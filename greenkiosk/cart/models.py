from django.db import models

# Create your models here.
class Shopping_cart(models.Model):
    name = models.CharField(max_length = 20)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField()
   
  




