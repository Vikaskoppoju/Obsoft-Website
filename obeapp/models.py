from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin


# Create your models here.
class Userform(models.Model):
    username= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    Designation= models.CharField(max_length=100)
    DateofJoinning= models.DateField()
    Biometricid= models.CharField(max_length=100,primary_key=True)
    password= models.CharField(max_length=100)
    permission = models.IntegerField(default=0)
class Departments(models.Model):
    department_name = models.CharField(max_length=100)
    department_id = models.CharField(max_length=100)
    department_hod_name = models.CharField(max_length=200)
    department_hod_id = models.CharField(max_length=100)
class Regulation(models.Model):
    Sno= models.IntegerField()
    Regulation= models.CharField(max_length=100)
    batch= models.CharField(max_length=50)
class Courses(models.Model):
    Sno= models.IntegerField()
    Coursenam= models.CharField(max_length=100)
    Coursecode= models.CharField(max_length=100)
    Regulation = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    semister = models.CharField(max_length=50)
    branch = models.CharField(max_length=100,default="-")

class CustomUser(AbstractUser, PermissionsMixin):
    sno = models.CharField(max_length=100, default=0)
    Designation = models.CharField(max_length=100)
    User_Name = models.CharField(max_length=200, default="None")
    Permissions = models.CharField(max_length=1000)
    Biometricid = models.CharField(max_length=100)
    branch = models.CharField(max_length=100, default="None")
    dept_id=models.CharField(max_length=100, default=0)
    hod=models.BooleanField(default=False)
    #email = models.EmailField(unique=True)

    # Remove 'username' and 'email' fields, as they are already provided by AbstractUser

    # Add this field to use 'email' as the unique identifier for the user
    #USERNAME_FIELD = 'email'

    # Add a unique related_name for the groups field
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',  # Use a unique related_name for the groups field
        related_query_name='custom_user'
    )

    # Add a unique related_name for the user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',  # Use a unique related_name for the user_permissions field
        related_query_name='custom_user'
    )

    def __str__(self):
        return self.email
#****************New******************
# class Userform(models.Model):
#     username= models.CharField(max_length=100)
#     email= models.CharField(max_length=100)
#     Designation= models.CharField(max_length=100)
#     DateofJoinning= models.DateField()
#     Biometricid= models.CharField(max_length=100,primary_key=True)
#     password= models.CharField(max_length=100)

# Create your models here.
class lessonplanBatch(models.Model):
    batch=models.CharField(max_length=20)
    academicyear=models.CharField(max_length=20)
    programme=models.CharField(max_length=20)
    semester=models.CharField(max_length=20)
    section=models.CharField(max_length=10)
    name_of_the_course=models.CharField(max_length=70)
    course_code=models.CharField(max_length=15)
    def __str__(self):
        return self.course_code
class courseoutcomes(models.Model):
    co=models.CharField(max_length=5,default='1')
    courseoutcome=models.CharField(max_length=100)
    knowledge_level=models.CharField(max_length=5,default='K1')
    course_code=models.CharField(max_length=15)
class textbooks(models.Model):
    sno=models.CharField(max_length=5,default=1)
    textbook_details=models.CharField(max_length=200)
    course_code=models.CharField(max_length=15)
class referencebooks(models.Model):
    sno=models.CharField(max_length=5,default='1')
    rfbook_details=models.CharField(max_length=200)
    course_code=models.CharField(max_length=15)
class targetproficiency(models.Model):
    co=models.CharField(max_length=15,default='')
    tpl=models.CharField(max_length=15,default='')
    l3=models.CharField(max_length=15,default='')
    l2=models.CharField(max_length=15,default='')
    l1=models.CharField(max_length=15,default='')
    #tpl=models.CharField(max_length=50,default="Target Proficiency Level")
    course_code=models.CharField(max_length=15)
class lectureplan(models.Model):
    sno=models.CharField(max_length=5,default='1')
    course_outcome=models.CharField(max_length=10,default='CO1')
    ilo=models.CharField(max_length=100,default='')
    knowledgelevel=models.CharField(max_length=5,default='')
    noof_hours=models.CharField(max_length=5,default='')
    pedagogy=models.CharField(max_length=50,default='')
    teachingaids=models.CharField(max_length=10,default='')
    course_code=models.CharField(max_length=15)
class co_pso_Matrix(models.Model):
    cos=models.CharField(max_length=10,default='')
    po1=models.CharField(max_length=10,default='')
    po2=models.CharField(max_length=10,default='')
    po3=models.CharField(max_length=10,default='')
    po4=models.CharField(max_length=10,default='')
    po5=models.CharField(max_length=10,default='')
    po6=models.CharField(max_length=10,default='')
    po7=models.CharField(max_length=10,default='')
    po8=models.CharField(max_length=10,default='')
    po9=models.CharField(max_length=10,default='')
    po10=models.CharField(max_length=10,default='')
    po11=models.CharField(max_length=10,default='')
    po12=models.CharField(max_length=10,default='')
    pso1=models.CharField(max_length=10,default='')
    pso2=models.CharField(max_length=10,default='')
    course_code=models.CharField(max_length=15)
class course_end_survey(models.Model):
    sno=models.CharField(max_length=5,default='1')
    cos=models.CharField(max_length=5,default='')
    question=models.CharField(max_length=100,default='')
    course_code=models.CharField(max_length=15)
class details_of_instructors(models.Model):
    sno=models.CharField(max_length=5,default='1')
    name=models.CharField(max_length=100,default='')
    designation=models.CharField(max_length=100,default='')
    year=models.CharField(max_length=20,default='')
    section=models.CharField(max_length=20,default='')
    contactno=models.CharField(max_length=30,default='')
    email=models.CharField(max_length=50,default='')
    course_code=models.CharField(max_length=15)
class teachers(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=80,default='sushma kurella')
    passwd=models.CharField(max_length=50)
    def __str__(self):
        return self.name


    