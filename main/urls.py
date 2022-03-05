from django.urls import path
from main.views import (
    StudentList,
    StudentDetail,
    StudentCreate,
    StudentUpdate,
    StudentDelete
)

urlpatterns = [
    path('',StudentList.as_view(),name="students"),
    path('student/<int:pk>/',StudentDetail.as_view(),name="student"),
    path('create-student/',StudentCreate.as_view(),name="create-student"),
    path('update-student/<int:pk>',StudentUpdate.as_view(),name="update-student"),
    path('delete-student/<int:pk>',StudentDelete.as_view(),name="delete-student")
]