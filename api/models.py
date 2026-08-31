from django.db import models

# Create your models here.
class teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

class student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

class course(models.Model):
    name = models.CharField(max_length=100)
    teacher_id = models.ForeignKey(teacher, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

class student_course(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(course, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)