from django.urls import path
from .views import ListCreateCourses

urlpatterns = [
    path('', ListCreateCourses.as_view()),
]
