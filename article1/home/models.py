from django.db import models

# Create your models here.
class Article(models.Model):
    name=models.CharField(max_length=50)
    descriptions=models.CharField(max_length=900)
    