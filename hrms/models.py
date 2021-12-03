from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import SET_NULL
from django.db.models.enums import Choices
from django.urls import reverse


# Create your models here.
class User(AbstractUser):
    thumb = models.ImageField()
    
class Department(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    history = models.TextField(max_length=1000, null=True, blank=True, default='No history')

    def __str__(self):
        return self.name

class Employee(models.Model):
    LANGUAGE  = (('english', 'ENGLISH'), ('hindi', 'HINDI'))
    GENDER = (('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER'))
    emp_id = models.CharField(max_length=50, default= 'emp'+str(range(1000, 5000, 1))+'in')
    thumb = models.ImageField(blank=True, null=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=120, null=True)
    address = models.CharField(max_length=100, default='')
    emergency = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER, max_length=20)
    department = models.ForeignKey(Department, on_delete=SET_NULL, null=True)
    joined = models.DateTimeField()
    language = models.CharField(choices=LANGUAGE, max_length=20, default='english')
    bank = models.CharField(max_length=30, default='Bank Name')
    salary = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.first_name

# class Attendance(models.Model):
#     STATUS = (('PRESENT', 'present'), ('ABSENT', 'absent'), ('UNAVAILABLE', 'unavailable'))
#     date = models.DateField(auto_now_add=True)
#     day_in = models.TimeField(null=True)
#     day_out = models.TimeField(null=True)
#     status = models.CharField(choices=STATUS, max_length=15)
#     staff = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

#     def save(self, *args, **kwargs):
#         self.day_in

class Leave (models.Model):
    STATUS = (('approved','APPROVED'),('unapproved','UNAPPROVED'),('decline','DECLINED'))
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    start = models.CharField(blank=False, max_length=15)
    end = models.CharField(blank=False, max_length=15)
    status = models.CharField(choices=STATUS,  default='Not Approved',max_length=15)

    def __str__(self):
        return self.employee + ' ' + self.start

class Recruitment(models.Model):
    first_name = models.CharField(max_length=25)
    last_name= models.CharField(max_length=25)
    position = models.CharField(max_length=15)
    email = models.EmailField(max_length=25)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name +' - '+self.position


    