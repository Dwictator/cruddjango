from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.
class inputProduct(models.Model):
   productname = models.TextField()
   productcategory = models.TextField()
   productdescription = models.TextField(max_length=200)
   productstock = models.IntegerField()
   #productimage = models.ImageField(upload_to='upload/')
   