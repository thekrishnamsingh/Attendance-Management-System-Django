from django.contrib import admin
from .models import Student,Faculty


# Register your models here.

class AdminStudent(admin.ModelAdmin):
    list_display=['name','rollno','course','teacher','semester','branch','present','absent','sr']
class AdminFaculty(admin.ModelAdmin):
    list_display=['name','username','password','dob','qualification','mobile','gender']
    
admin.site.register(Student,AdminStudent)
admin.site.register(Faculty,AdminFaculty)