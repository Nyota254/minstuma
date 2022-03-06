from email.policy import HTTP
from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
                                        CreateView,
                                        UpdateView,
                                        DeleteView,
                                        FormView
)
from django.urls import reverse_lazy
from main.models import Student
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializer import StudentSerializer

class CustomLoginView(LoginView):
    '''
    Login Page Customized View
    '''
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('students')

class RegisterPage(FormView):
    '''
    Class View to allow registration of user
    '''
    template_name = 'main/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('students')

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('students')
        return super(RegisterPage,self).get(*args,**kwargs)


class StudentList(LoginRequiredMixin,ListView):
    '''
    Class view to list students
    '''
    model = Student
    context_object_name = 'students'

    def get_context_data(self,**kwargs):
        context =super().get_context_data(**kwargs)
        context['students'] = context['students'].filter(user=self.request.user)

        search_value = self.request.GET.get('search-area') or ''
        if search_value:
            context['students'] = context['students'].filter(first_name__icontains=search_value)

        context['search_value'] = search_value
        return context

class StudentDetail(LoginRequiredMixin,DetailView):
    '''
    Class View to display student detail
    '''
    model = Student
    context_object_name = 'student'

class StudentCreate(LoginRequiredMixin,CreateView):
    '''
    Class View to add new student
    '''
    model = Student
    fields = ['first_name','second_name','course','notes','course_complete']
    success_url = reverse_lazy('students')

    def form_valid(self,form):
        '''Data for user field ommitted on fields display'''
        form.instance.user = self.request.user
        return super(StudentCreate,self).form_valid(form)

class StudentUpdate(LoginRequiredMixin,UpdateView):
    '''
    Class View to display form to update student details
    '''
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students')

class StudentDelete(LoginRequiredMixin,DeleteView):
    '''
    Class View to allow deletion of a student
    '''
    model = Student
    context_object_name = 'student'
    success_url = reverse_lazy('students')

class StudentListApi(APIView):
    '''
    Api to give data on students
    '''
    def get(self,request):
        all_students = Student.objects.all() 
        serializers = StudentSerializer(all_students,many=True)
        return Response(serializers.data)

