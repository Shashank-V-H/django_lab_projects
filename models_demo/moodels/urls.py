from django.urls import path,include
from . import views

urlpatterns = [
    path('test/',views.test,name="test"),
    path('register/',views.register,name="register"),
    # path('registered/<int:course_id>/',views.registered,name="registered"),
    path('registered/<str:course_title>/', views.registered, name='registered'),
]