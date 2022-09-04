from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="teacher")
    students = models.ManyToManyField(User, related_name="students")
    created = models.DateField(auto_now_add=True)
    schedule = models.TimeField()

    def __str__(self):
        return self.name

class classAttendence(models.Model):
    module = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.module.name + "__" +str(self.date)

class Attendence(models.Model):
    classAttendance = models.ForeignKey(classAttendence, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False)
    student = models.ForeignKey(User, related_name="student", null=True ,on_delete=models.CASCADE)
    module = models.ForeignKey(Class, related_name="module", on_delete=models.CASCADE, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.first_name}_{self.status}"
