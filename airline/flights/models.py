from django.db import models

# Create your models here.
class AIRPORT(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} ({self.code})" 

class  FLIGHT(models.Model):
    origin=models.ForeignKey(AIRPORT,on_delete=models.CASCADE,related_name="depatures")
    destination=models.ForeignKey(AIRPORT,on_delete=models.CASCADE,related_name="arrivals")
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.id}:{self.origin} to {self.destination}"