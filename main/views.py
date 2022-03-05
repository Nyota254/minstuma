from email.policy import HTTP
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
                                        CreateView,
                                        UpdateView,
                                        DeleteView
)
from django.urls import reverse_lazy
from main.models import Student

class StudentList(ListView):
    model = Student
    context_object_name = 'students'

class StudentDetail(DetailView):
    model = Student
    context_object_name = 'student'

class StudentCreate(CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students')

class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students')

class StudentDelete(DeleteView):
    model = Student
    context_object_name = 'student'
    success_url = reverse_lazy('students')

