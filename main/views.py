from email.policy import HTTP
from django.shortcuts import render
from django.views.generic.list import ListView
from main.models import Student

class StudentList(ListView):
    model = Student
    context_object_name = 'students'

