
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class User_info(models.Model):
   user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   contact = models.CharField(max_length=100)
   address = models.CharField(max_length=100)

class Pharmacy(models.Model):
   user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   contact = models.CharField(max_length=100)
   address = models.CharField(max_length=100)


class Medicine(models.Model):
    user = models.ForeignKey(Pharmacy,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    t_quantity = models.CharField(max_length=100,null=True)
    half_qty = models.CharField(max_length=100,null=True)
    exp_date = models.CharField(max_length=100,null=True)
    half_date = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)
    companyname = models.CharField(max_length=100,null=True)
    medtype = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='images/',null=True)


class Booking(models.Model):
     user = models.ForeignKey(User_info,on_delete=models.CASCADE)
     medicine = models.ForeignKey(Medicine,on_delete=models.CASCADE)
     status = models.CharField(max_length=100)
     total = models.CharField(max_length=100, null=True)
     payment = models.CharField(max_length=100, null=True)
     quantity = models.CharField(max_length=100, null=True)
     delivery = models.CharField(max_length=100, null=True)


class Complaint(models.Model):
    user = models.ForeignKey(User_info, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)

class MedBook(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    med_qty = models.CharField(max_length=100)
    payment = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    delivery = models.CharField(max_length=100)
    price = models.CharField(max_length=100,null=True)

