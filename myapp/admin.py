from django.contrib import admin
from .models import Student,Faculty




class AdminStudent(admin.ModelAdmin):
    list_display=['name','rollno','course','teacher','semester','branch','present','absent','sr']
class AdminFaculty(admin.ModelAdmin):
    list_display=['name','username','password','dob','qualification','mobile','gender']
    
