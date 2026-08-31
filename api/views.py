from django.shortcuts import render
from .models import teacher, student, student_course, course

# Create your views here.
def teacher_list(request):
    teachers = teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def student_list(request):
    students = student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def course_list(request):
    courses = course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def student_course_list(request):
    student_courses = student_course.objects.all()
    return render(request, 'student_course_list.html', {'student_courses': student_courses})