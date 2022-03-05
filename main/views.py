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

class CustomLoginView(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('students')

class RegisterPage(FormView):
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
    model = Student
    context_object_name = 'student'

class StudentCreate(LoginRequiredMixin,CreateView):
    model = Student
    fields = ['first_name','second_name','course','notes','course_complete']
    success_url = reverse_lazy('students')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(StudentCreate,self).form_valid(form)

class StudentUpdate(LoginRequiredMixin,UpdateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students')

class StudentDelete(LoginRequiredMixin,DeleteView):
    model = Student
    context_object_name = 'student'
    success_url = reverse_lazy('students')

