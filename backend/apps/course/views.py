from django.db.models import query
from rest_framework import generics, permissions
from .serializers import CourseSerialize
from .models import Course


class ListCreateCourses(generics.ListCreateAPIView):
    serializer_class = CourseSerialize
    queryset = Course.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    