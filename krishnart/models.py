from django.db import models

class Drawings(models.Model):
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')  
    date = models.DateField()

    def __str__(self):
        return self.name

