from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from .models import Student, Course
from django.views.generic import ListView, DetailView
from django.views import View
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io


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


# generic class view


class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'  # Specify your template name/location
    context_object_name = 'students'  # Name to use for the list of objects in the template

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'  # Specify your template name/location
    context_object_name = 'student'  # Name to use for the single object in the template



# for csv file generation

class ExportCSVView(View):
    def get(self, request):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="students.csv"'

        writer = csv.writer(response)
        writer.writerow(['Name', 'Email'])

        students = Student.objects.all()
        for student in students:
            writer.writerow([student.name, student.email])

        return response


# for pdf generation

class ExportPDFView(View):
    def get(self, request):
        # Create the HttpResponse object with the appropriate PDF header.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="students.pdf"'

        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.setFont("Helvetica", 12)

        students = Student.objects.all()
        y = 750
        for student in students:
            p.drawString(30, y, f"Name: {student.name}, Email: {student.email}")
            y -= 20

        p.showPage()
        p.save()

        buffer.seek(0)
        return HttpResponse(buffer, content_type='application/pdf')