from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
	name = models.CharField(max_length=200, null=False, blank=False)
	email = models.EmailField(max_length=60,null=False, blank=False)
	phone = models.CharField(max_length=15,null=False, blank=False)
	address = models.CharField(max_length=1000, null=False, blank=False)
	photo = models.ImageField()
	department= models.CharField(max_length=100,null=False, blank=False)
	age = models.IntegerField(null=False, blank=False)
	is_married = models.BooleanField(null=False, blank=False, default=False)
	dob = models.DateField(null=False, blank=False)
	is_working = models.BooleanField(null=False, blank=False,default=True)
	date_of_joining = models.DateField(null = False,blank=False)
	date_of_leaving = models.DateField(null = False,blank=False)
	salary = models.CharField(max_length=10,null = False,blank=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

