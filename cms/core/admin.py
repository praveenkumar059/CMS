from django.contrib import admin
from .models import StudentProfile
from .models import Attendance,Result,Fees,Message

admin.site.register(StudentProfile)
admin.site.register(Attendance)
admin.site.register(Result)
admin.site.register(Fees)
admin.site.register(Message)



