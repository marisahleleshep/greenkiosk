from django.db import models

# Create your models here.
class Display_item(models.Model):
    name=models.CharField(max_length=20)

    def all_names():
        return Display_item.objects.all()
    def __str__(self):
        return self.name
        
    
    
    