from django.db import models

# Create your models here.
class User_Signup(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    profileimg = models.ImageField(upload_to='images/',default="images/user.png")  
   
   

    def __str__(self):
        return self.name
class Verification(models.Model):
    vid= models.AutoField(primary_key=True)
    uname=models.CharField(max_length=200)
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
    passportimg = models.ImageField(upload_to='images/')     
    selfieimg = models.ImageField(upload_to='images/')     
    idbackimg = models.ImageField(upload_to='images/')     
    documentwithaddimg = models.ImageField(upload_to='images/')     
     
    
    def __str__(self):
        return self.uname
    