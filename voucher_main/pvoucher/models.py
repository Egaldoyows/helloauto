from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    date = models.DateField(auto_now_add=True)
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=250)
    audience= models.CharField(max_length=20)
    read=models.BooleanField(blank=True)
    
    def __str__(self):
        return str(self.subject)
        
    
class Vouchers(models.Model):
    receipient=models.CharField(max_length=200)
    account = models.CharField(max_length=200)
    desc1=models.CharField(max_length=200)
    desc2 =models.CharField(max_length=200,blank=True)
    desc3 =models.CharField(max_length=200,blank=True)
    amount1=models.IntegerField(blank=True, null=True)
    amount2=models.IntegerField(blank=True, null=True)
    amount3=models.IntegerField(blank=True, null=True)
    total=models.IntegerField(max_length=10)
    payment_mode=models.CharField(max_length=10)
    project=models.CharField(max_length=20)
    currency=models.CharField(max_length=10)
    invoice_no = models.CharField(max_length=10,default='n/a')
    date_created=models.DateTimeField(auto_now_add=True)
    payment_date=models.DateField()
    prepared=models.CharField(max_length=50,blank=True)
    approved=models.CharField(max_length=50,blank=True)
    company=models.CharField(max_length=50,blank=True)
    comment=models.CharField(max_length=50,blank=True)
    
    
    def __str__(self):
        return str(self.receipient)
    
    
class Projects(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.name)
