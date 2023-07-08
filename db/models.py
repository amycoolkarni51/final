''' Added By :-  Shruti Bathe
    Task :-  database table
    Models:- 
       class Contact :- contact table
       class signup  :- signup table
       class login   :- login table'''

from django.db import models

# Create your models here.

# contact table
class Contact(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    EmailId = models.EmailField()
    Location = models.TextField(max_length=100)
    Message = models.TextField(max_length=255)
    
    class Meta:
        db_table="contact"
        
# signup table
class SignUp(models.Model):
    Full_Name = models.CharField(max_length=20)
    EmailId = models.EmailField()
    Password = models.CharField(max_length=20)
    Confirm_Password = models.CharField(max_length=20)
    
    class Meta:
        db_table="signup"
        
# login table
class login(models.Model):
    EmailId = models.EmailField()
    Password = models.CharField(max_length=20)
    
    class Meta:
        db_table="login"
        

'''
   Added By:-  Shruti Bathe
   Task    :-  Created Register Database table
   Model   :- 
            class Register :- Register Table '''
from django.db import models

# Create your models here.
# Register table
class Registeration(models.Model):
    Full_Name = models.CharField(max_length=20)
    EmailId = models.EmailField()
    Mobile = models.BigIntegerField()
    Gender = models.CharField(max_length=10)
    City = models.CharField(max_length=30)
    Qualification = models.CharField(max_length=30)
    Profession = models.CharField(max_length=30)
    Courses = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    Status = models.CharField(max_length=30)
    class Meta:
        db_table="registeration"
        
    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_desc = models.CharField(max_length=1000)
    syllabus_pdf= models.CharField(max_length=1000)
    introduction_link= models.CharField(max_length=1000)
    pdf_link = models.CharField(max_length=1000)
    video_link = models.CharField(max_length=1000)
    select_course=models.CharField(max_length=1000)
    filename=models.CharField(max_length=1000)
    
    class Meta:
        db_table="course"
        