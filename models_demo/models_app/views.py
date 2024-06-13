from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from .models import Student, Course

# Create your views here.
def test(request):
    return HttpResponse("this is a test")


def register(request):
    if request.method == 'POST':
        student_name = request.POST['name']
        student_email = request.POST['email']
        course_id = request.POST['course']
        course = Course.objects.get(pk=course_id)
        student, created = Student.objects.get_or_create(name=student_name, email=student_email)
        course.students.add(student)
        messages.success(request, 'Student successfully added to the course.')
        return redirect('register')
    else:
        courses = Course.objects.all()
        return render(request, 'register.html', {'courses': courses})

def registered(request, course_title):
    course = get_object_or_404(Course, title=course_title)
    students = course.students.all()
    return render(request, 'registered.html', {'course': course, 'students': students})
        
