from django.db import models

# Create your models here.
class Project(models.Model):
    #Images
    image = models.ImageField(upload_to='images/')
    #Project Summary
    projectInfo = models.CharField(max_length=250)


