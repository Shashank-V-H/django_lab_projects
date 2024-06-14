from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project
from .forms import ProjectForm

def register_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('project_success')  # Redirect to a success page or another view
            messages.success(request, 'Student successfully added to the course.')
            return redirect('register_project')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

def project_success(request):
    return render(request, 'project_success.html')