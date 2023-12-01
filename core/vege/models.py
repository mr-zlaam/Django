from django.db import models


# Create your models here.
class Recipe(models.Model):
    racipe_name = models.CharField(max_length=200)
    racipe_description = models.TextField()
    racipe_image = models.ImageField(upload_to="recipe")
