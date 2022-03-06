from django.urls import path
from django.contrib.auth.views import LogoutView
from main.views import (
    StudentList,
    StudentDetail,
    StudentCreate,
    StudentUpdate,
    StudentDelete,
    CustomLoginView,
    RegisterPage,
    StudentListApi
)

urlpatterns = [
    path('',StudentList.as_view(),name="students"),
    path('student/<int:pk>/',StudentDetail.as_view(),name="student"),
    path('create-student/',StudentCreate.as_view(),name="create-student"),
    path('update-student/<int:pk>',StudentUpdate.as_view(),name="update-student"),
    path('delete-student/<int:pk>',StudentDelete.as_view(),name="delete-student"),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('api/students',StudentListApi.as_view())
]