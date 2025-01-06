from email.policy import default
import json
from django.db import models

# Create your models here.
from django.db import models
class Logintable(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)  

class UserTable(models.Model):
    LOGIN=models.ForeignKey(Logintable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, blank=True, null=True)
    Address = models.CharField(max_length=300, blank=True, null=True)
    Phone= models.BigIntegerField(null=True, blank=True)
    Email = models.CharField(max_length=30, blank=True, null=True)
    Vehiclenumber = models.CharField(max_length=30, blank=True, null=True)

class StationTable(models.Model):
    LOGIN=models.ForeignKey(Logintable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    Email = models.CharField(max_length=30, blank=True, null=True)
    StationNumber = models.CharField(max_length=30, blank=True, null=True)

class ServiceTable(models.Model):
    LOGIN=models.ForeignKey(Logintable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, blank=True, null=True) 
    Email = models.CharField(max_length=30, blank=True, null=True)
    Phone = models.BigIntegerField(blank=True, null=True)
    Address = models.CharField(max_length=30, blank=True, null=True)

class FeedbackTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    Chargingstation = models.ForeignKey(StationTable, on_delete=models.CASCADE,null=True,blank=True)
    Feedback = models.CharField(max_length=30, blank=True, null=True)
    Date = models.DateField(auto_now_add=True, blank=True,null=True )
    Rate = models.CharField(max_length=30, blank=True ,null=True)

class ComplaintTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    Complaint = models.CharField(max_length=100, blank=True, null=True)
    Description = models.CharField(max_length=100, blank=True, null=True)
    Category = models.CharField(max_length=100, blank=True, null=True)
    Date = models.DateField(auto_now_add=True, blank=True, null=True)
    Reply = models.CharField(max_length=100, blank=True, null=True)

class SpareTable(models.Model):
    STATION = models.ForeignKey(StationTable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, blank=True, null=True)
    Amount = models.IntegerField(blank=True, null=True)
    Details = models.CharField(max_length=30, blank=True, null=True)

class SlotTable(models.Model):
    STATION = models.ForeignKey(StationTable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, blank=True, null=True)
    Amount = models.IntegerField(blank=True, null=True)
    Details = models.TextField(max_length=30, blank=True, null=True)
    Status = models.CharField(max_length=30, blank=True, null=True)
       
class SpareBookingTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)   
    SLOT = models.ForeignKey(SlotTable, on_delete=models.CASCADE)   
    SpareName = models.CharField(max_length=30, blank=True, null=True)
    Amount = models.IntegerField(blank=True, null=True)
    Quantity = models.IntegerField(blank=True, null=True)
    Status = models.CharField(max_length=30, blank=True, null=True)

