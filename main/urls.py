from django.urls import path
from . import views

urlpatterns = [
    path('',views.studentList,name="students")
]