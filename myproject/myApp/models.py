from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    full_name=models.CharField(max_length=100,null=True)
    mobile_number=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=100,null=True)
    age=models.PositiveIntegerField(null=True)
    present_address=models.TextField(null=True)
    permanent_address=models.TextField(null=True)
    last_education_name=models.CharField(max_length=100,null=True)
    institute_name=models.CharField(max_length=100,null=True)
    passing_year=models.IntegerField(null=True)
    grade=models.CharField(max_length=100,null=True)
    profile_image=models.ImageField(upload_to="media/image",null=True)
    date_of_birth=models.DateField(null=True)