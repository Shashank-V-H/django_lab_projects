from django import forms
from .models import Project, Student

class ProjectForm(forms.ModelForm):
      student_name = forms.CharField(max_length=50, required=True, label='Student Name')

      class Meta:
            model = Project
            fields = ['student_name', 'topic', 'languages', 'duration']

      def save(self, commit=True):
            student_name = self.cleaned_data['student_name']
            student, created = Student.objects.get_or_create(name=student_name)
            self.instance.student = student
            return super().save(commit=commit)