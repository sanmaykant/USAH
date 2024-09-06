from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from college.models import Department, Course

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email field is required!!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = [
        ('professor', 'Professor'),
        ('student', 'Student'),
    ]

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class ProfessorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(
            Department, to_field="dept_code", on_delete=models.CASCADE)

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    graduation_year = models.PositiveIntegerField()

class StudentEnrollment(models.Model):
    user = models.ForeignKey(StudentProfile, to_field="user",
                             on_delete=models.CASCADE)
    course = models.ForeignKey(Course, to_field="course_code",
                               on_delete=models.CASCADE)
    class Meta:
        unique_together = ("user", "course")
