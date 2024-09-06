from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ProfessorProfileViewSet, StudentProfileViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'professor-profiles', ProfessorProfileViewSet)
router.register(r'student-profiles', StudentProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
