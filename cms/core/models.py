from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    register_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=5)
    current_semester = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.register_number} - {self.user.get_full_name() or self.user.username}"
    
class Attendance(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    semester = models.PositiveSmallIntegerField()
    subject_code = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=100)
    attendance_percentage = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.student.register_number} - Sem {self.semester}"


    
class Result(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    semester = models.IntegerField()
    subject_code = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=5)
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.student.register_number} - Sem {self.semester}"


class Fees(models.Model):
    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    total_fee = models.PositiveIntegerField()
    paid_amount = models.PositiveIntegerField()

    def due_amount(self):
        return self.total_fee - self.paid_amount

    def __str__(self):
        return self.student.register_number
    
class Message(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


   

