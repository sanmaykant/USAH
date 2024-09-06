from django.contrib import admin
from .models import CustomUser, ProfessorProfile, StudentProfile

admin.site.register(CustomUser)
admin.site.register(ProfessorProfile)
admin.site.register(StudentProfile)
