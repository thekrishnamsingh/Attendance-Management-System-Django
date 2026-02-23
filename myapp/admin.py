from django.contrib import admin
from .models import Student,Faculty




class AdminStudent(admin.ModelAdmin):
    list_display=['name','rollno','course','teacher','semester','branch','present','absent','sr']

admin.site.register(Student,AdminStudent)
admin.site.register(Faculty,AdminFaculty)