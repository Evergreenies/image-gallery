from django.db import models

# Create your models here.

class UploadImage(models.Model):
    name = models.TextField(max_length=20)
    description = models.TextField(max_length=100)
    image = models.ImageField(max_length=300)
    category = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.name, self.description, self.image, self.category
