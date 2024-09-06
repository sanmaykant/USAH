from rest_framework import serializers
from .models import CustomUser, ProfessorProfile, StudentProfile

class ProfessorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorProfile
        fields = ['user', 'department', 'role']

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['user', 'major', 'graduation_year']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
                    'id',
                    'email',
                    'first_name',
                    'last_name',
                    'is_active',
                    'user_type'
                ]
