from rest_framework import viewsets, permissions
from .models import CustomUser, ProfessorProfile, StudentProfile
from .serializers import CustomUserSerializer, ProfessorProfileSerializer, StudentProfileSerializer
from .permissions import IsProfessor, IsStudent

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Base permission

class ProfessorProfileViewSet(viewsets.ModelViewSet):
    queryset = ProfessorProfile.objects.all()
    serializer_class = ProfessorProfileSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsProfessor]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsProfessor]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsStudent]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsStudent]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
