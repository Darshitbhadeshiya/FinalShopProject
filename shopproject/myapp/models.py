from django.db import models


# Create your models here.
#admin username=darshit,password=dashupython
class signup(models.Model):
   #created=models.DateTimeField(auto_now_add=True)
    Firstname=models.CharField(max_length=20)
    Lastname=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    Mobile=models.BigIntegerField()


class product(models.Model):
    image = models.ImageField(upload_to='static/sideimage')
    title = models.CharField(max_length=20)
    discription = models.TextField()
    price = models.BigIntegerField()
    created_at = models.DateField(auto_now_add=True)
    

class ImageModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/images')