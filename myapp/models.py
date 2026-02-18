from django.db import models

# Create your models here.


class Faculty(models.Model):
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=30)
    dob=models.DateField()
    qualification=models.CharField(max_length=20)
    mobile=models.IntegerField()
    gender=models.CharField(max_length=6)
    @staticmethod
    def is_exist(mail):
        return Faculty.objects.filter(username=mail)

class Student(models.Model):
    teacher = models.CharField(max_length=50)
    name=models.CharField(max_length=30)
    rollno=models.CharField(max_length=5,null=True,default=0)
    course=models.CharField(max_length=20,null=True)
    semester=models.CharField(max_length=10)
    branch=models.CharField(max_length=20)
    present=models.IntegerField(default=0,blank=True,null=True)
    absent=models.IntegerField(default=0,blank=True,null=True)
    sr=models.AutoField(primary_key=True)