from rest_framework.serializers import ModelSerializer
from .models import Course


class CourseSerialize(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
