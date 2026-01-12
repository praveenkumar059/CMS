from django.urls import path
from .views import login_view, student_dashboard, admin_dashboard, logout_view
from .views import student_profile, student_attendance,student_results,student_fees,student_messages
from .views import admin_dashboard ,admin_add_student, admin_attendance,admin_results,admin_fees,admin_messages

 







urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('student/dashboard/', student_dashboard, name='student_dashboard'),
    path('student/profile/', student_profile, name='student_profile'),
    path('student/attendance/', student_attendance, name='student_attendance'),
    path('student/results/', student_results, name='student_results'),
    path('student/fees/', student_fees, name='student_fees'),
    path('student/messages/', student_messages, name='student_messages'),



    path('admin-panel/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin-panel/add-student/', admin_add_student, name='admin_add_student'),
    path('admin-panel/attendance/', admin_attendance, name='admin_attendance'),
    path('admin-panel/results/', admin_results, name='admin_results'),
    path('admin-panel/fees/', admin_fees, name='admin_fees'),
    path('admin-panel/messages/', admin_messages, name='admin_messages'),





    

    
]
