from django.db import models

# Create your models here.

# Existing Student model
class Student(models.Model):
    name = models.CharField(max_length=50)
    # email = models.EmailField(unique=False)

    def __str__(self):
        return self.name

# New Project model
class Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='projects')
    topic = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(help_text='Duration in months')

    def __str__(self):
        return f'{self.topic} by {self.student.name}'
