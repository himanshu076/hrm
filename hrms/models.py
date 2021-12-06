from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.deletion import SET_NULL
from django.db.models.enums import Choices
from django.urls import reverse


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, fullname=None, birthday=None, zipcode=None,password=None
                    ):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            Email_Address=self.normalize_email(email),
            name=self.normalize_email(email),
            Date_of_Birth=birthday,
            zipcode=zipcode,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Email_Address, password):
        user = self.create_user(
            Email_Address=self.normalize_email(Email_Address),
            password=password,
        )
        user.is_admin = True
        user.is_active=True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class Users(AbstractBaseUser):
    Email_Address = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True, null=True, default=None)
    Date_of_Birth = models.CharField(max_length=30, blank=True, null=True, default=None)
    name = models.CharField(max_length=30, blank=True, null=True)
    username= models.CharField(max_length=30,unique=True, blank=True, null=True)
    zipcode = models.CharField(max_length=30, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_super_teacher = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'Email_Address'

    objects = MyAccountManager()

    class Meta:
        db_table = "tbl_users"

    def __str__(self):
        return str(self.email)


    def has_perm(self, perm, obj=None): return self.is_superuser

    def has_module_perms(self, app_label): return self.is_superuser




# class User(AbstractUser):
#     thumb = models.ImageField()
    
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
    bank = models.CharField(max_length=30, default='Enter Bank Name')
    salary = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['created']

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


    # https://medium.com/geekculture/register-login-and-logout-users-in-django-rest-framework-51486390c29