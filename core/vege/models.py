from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    racipe_name = models.CharField(max_length=200)
    racipe_description = models.TextField()
    racipe_image = models.ImageField(upload_to="recipe")
