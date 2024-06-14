from django.urls import path
from . import views

urlpatterns = [
    path('register_project/', views.register_project, name='register_project'),
]