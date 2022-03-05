from django.urls import path
from main.views import (
    StudentList
)

urlpatterns = [
    path('',StudentList.as_view(),name="students")
]