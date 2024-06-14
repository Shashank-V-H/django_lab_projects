from django.urls import path,include
from . import views

urlpatterns = [
    path('test/',views.test,name="test"),
    path('register/',views.register,name="register"),
    path('registered/<str:course_title>/', views.registered, name='registered'),
]