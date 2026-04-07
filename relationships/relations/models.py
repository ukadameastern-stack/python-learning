from django.db import models

# Create your models here.

class Husband(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        
class Wife(models.Model):
    name = models.CharField(max_length=255)
    husband = models.OneToOneField(Husband, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " is wife of " + self.husband.name
 