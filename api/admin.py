from django.contrib import admin
from .models import teacher, student, student_course, course

# Register your models here.
admin.site.register(teacher)
admin.site.register(student)
admin.site.register(student_course)
admin.site.register(course)