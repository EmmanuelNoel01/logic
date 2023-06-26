from django.db import models

# Create your models here.
class Sender(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=200,null=True)
    Package=models.CharField(max_length=20,null=True)
    destination=models.TextField(max_length=20,blank=False)

def __str__(self):
   return self.name

class Recipient(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    contact=models.CharField(max_length=200,null=True)

def __str__(self):
    return self.name

class Courier(models.Model):
   name=models.CharField(max_length=20)
   contact=models.CharField(max_length=200,null=True)
   email=models.CharField(max_length=200,null=True)

def __str__(self):
   return self.name

class Admin(models.Model):
    name=models.CharField(max_length=20)
    contact=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)

def __str__(self):
   return self.name  

class WarehouseAdmin(models.Model):
    name=models.CharField(max_length=20)
    contact=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    city=models.CharField(max_length=20,null=True)

def __str__(self):
   return self.name 