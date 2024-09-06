from rest_framework import viewsets, permissions
from .models import Department, Course
from .serializers import DepartmentSerializer, CourseSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer 
