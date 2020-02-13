from django.db import models

# Create your models here.
class User_Signup(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    fullname = models.CharField(max_length=255,default="")
    middlename = models.CharField(max_length=255,default="")
    lastname = models.CharField(max_length=255,default="")
    address1 = models.CharField(max_length=255,default="")
    address2 = models.CharField(max_length=255,default="")
    
    zipcode = models.PositiveSmallIntegerField(default=0)
    city = models.CharField(max_length=255,default="")
    region = models.CharField(max_length=255,default="")
    country = models.CharField(max_length=255,default="")
    
    dob = models.PositiveSmallIntegerField(default=0)
    passid = models.PositiveSmallIntegerField(default=0)
    date_of_issue = models.PositiveSmallIntegerField(default=0)
    expiringdate = models.PositiveSmallIntegerField(default=0)
   

    def __str__(self):
        return self.name
    