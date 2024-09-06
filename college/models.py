from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=75, unique=True)
    dept_code = models.CharField(max_length=10, unique=True, primary_key=True)

class Course(models.Model):
    dept_code = models.ForeignKey(Department, to_field="dept_code", on_delete=models.CASCADE)
    course_name = models.CharField(max_length=75, unique=True)
    course_code = models.CharField(max_length=25, unique=True)
    class Meta:
        unique_together = ("dept_code", "course_code")
