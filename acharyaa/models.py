from django.db import models
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.IntegerField(max_length=12)
    description=models.TextField()

def __str__ (self):
    return self.email    

class Enrollment(models.Model):        
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    Gender=models.CharField(max_length=25)
    PhoneNumber=models.CharField(max_length=12)
    DOB=models.CharField(max_length=50)
    SelectMembershipPlan=models.CharField(max_length=200)
    Reference=models.CharField(max_length=55)
    paymentStatus=models.CharField(max_length=55,blank=True,null=True)
    Price=models.IntegerField(max_length=55,blank=True,null=True)
    DueDate=models.DateTimeField(blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True,)

    def __str__(self):
        return self.FullName

class MembershipPlan(models.Model):
    plan=models.CharField(max_length=185)
    price=models.IntegerField(max_length=55)

    def __int__(self):
        return self.id

class Gallery(models.Model):
    tittle=models.CharField(max_length=100)
    img=models.ImageField(upload_to="gallery")
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
    def __int__(self):
        return self.id

    