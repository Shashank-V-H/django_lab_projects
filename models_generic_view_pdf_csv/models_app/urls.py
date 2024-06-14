from django.urls import path,include
from . import views
from .views import StudentListView, StudentDetailView
from .views import ExportCSVView , ExportPDFView


urlpatterns = [
    path('test/',views.test,name="test"),
    path('register/',views.register,name="register"),
    # path('registered/<int:course_id>/',views.registered,name="registered"),
    path('registered/<str:course_title>/', views.registered, name='registered'),
    # urls for generice class view
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    # urls for csv and pdf generation
    path('export/csv/', ExportCSVView.as_view(), name='export_csv'),
    path('export/pdf/', ExportPDFView.as_view(), name='export_pdf'),


]