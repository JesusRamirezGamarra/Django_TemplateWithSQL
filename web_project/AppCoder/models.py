from django.db import models
# from datetime import date
from django.utils import timezone
from datetime import datetime

# Create your models here.

# class Donation(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#     dateofbirht = models.DateField()
#     collaboration = models.IntegerField()
#     bio = models.CharField(max_length=500)
#     JobRol = models.CharField(max_length=20)
#     development =models.BooleanField()
#     design =models.BooleanField()
#     business =models.BooleanField()

    

class Donation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    dateofbirht = models.DateField()
    bio = models.CharField(max_length=500)
    createdate = models.DateTimeField(auto_now_add=True)
    # createdate = models.DateTimeField(default=datetime.now())
    #createdate = models.DateField( null=True)
    #createdate = models.DateField(default=date.today())
    # createdate = models.DateField(default=django.utils.timezone.now())
    

    def __str__(self):
        return "%s %s" % (self.name,self.email)    

class Collaboration(models.Model):
    payment = models.IntegerField()
    createdate = models.DateTimeField(auto_now_add=True)
    # createdate = models.DateTimeField(default=datetime.now())
    #createdate = models.DateField( null=True)
    # createdate = models.DateField(default=date.today())
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s %s" % (self.payment,self.createdate)    
    
class Job(models.Model):    
    # user_JobWorked = models.CharField(max_length=50)    
    jobrol = models.CharField(max_length=20)
    development =models.BooleanField()
    design =models.BooleanField()
    business =models.BooleanField()
    createdate = models.DateTimeField(auto_now_add=True)
    # createdate = models.DateTimeField(default=datetime.now())
    #createdate = models.DateField( null=True)    
    # createdate = models.DateField(default=date.today())
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.jobrol        