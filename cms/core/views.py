from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import StudentProfile, Attendance, Result, Fees,Message
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib import messages



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid login'})

    return render(request, 'auth/login.html')


@login_required
def student_dashboard(request):
    return render(request, 'student/dashboard.html')


@login_required
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def student_profile(request):
    profile = get_object_or_404(StudentProfile, user=request.user)
    return render(request, 'student/profile.html', {'profile': profile})

@login_required
def student_attendance(request):
    profile = get_object_or_404(StudentProfile, user=request.user)
    attendance_list = Attendance.objects.filter(student=profile)

    return render(
        request,
        'student/attendance.html',
        {'attendance_list': attendance_list}
    )

@login_required
def student_results(request):
    profile = get_object_or_404(StudentProfile, user=request.user)
    semester = request.GET.get('semester')

    results = []
    cgpa = None

    if semester:
        results = Result.objects.filter(
            student=profile,
            semester=semester
        )

        # simple CGPA calculation
        grade_points = {
            'O': 10, 'A+': 9, 'A': 8,
            'B+': 7, 'B': 6, 'C': 5
        }

        total_points = 0
        total_credits = 0

        for r in results:
            gp = grade_points.get(r.grade, 0)
            total_points += gp * r.credits
            total_credits += r.credits

        if total_credits > 0:
            cgpa = round(total_points / total_credits, 2)

    return render(
        request,
        'student/results.html',
        {
            'results': results,
            'cgpa': cgpa,
            'selected_semester': semester
        }
    )

@login_required
def student_fees(request):
    profile = get_object_or_404(StudentProfile, user=request.user)
    fees = get_object_or_404(Fees, student=profile)

    return render(
        request,
        'student/fees.html',
        {'fees': fees}
    )

@login_required
def student_messages(request):
    messages = Message.objects.order_by('-created_at')
    return render(
        request,
        'student/messages.html',
        {'messages': messages}
    )


@staff_member_required
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')


@staff_member_required
def admin_add_student(request):
    if request.method == 'POST':
        reg_no = request.POST['register_number']
        password = request.POST['password']
        name = request.POST['name']
        department = request.POST['department']
        phone = request.POST['phone']
        blood = request.POST['blood']
        semester = request.POST['semester']

        # create user
        user = User.objects.create_user(
            username=reg_no,
            password=password,
            first_name=name
        )

        # create student profile
        StudentProfile.objects.create(
            user=user,
            register_number=reg_no,
            department=department,
            phone_number=phone,
            blood_group=blood,
            current_semester=semester
        )

        messages.success(request, 'Student added successfully')
        return redirect('admin_dashboard')

    return render(request, 'admin/add_student.html')

@staff_member_required
def admin_attendance(request):
    students = StudentProfile.objects.all()

    if request.method == 'POST':
        student_id = request.POST['student']
        semester = request.POST['semester']
        subject_code = request.POST['subject_code']
        subject_name = request.POST['subject_name']
        percentage = request.POST['percentage']

        student = StudentProfile.objects.get(id=student_id)

        Attendance.objects.create(
            student=student,
            semester=semester,
            subject_code=subject_code,
            subject_name=subject_name,
            attendance_percentage=percentage
        )

        return redirect('admin_dashboard')

    return render(
        request,
        'admin/attendance.html',
        {'students': students}
    )

@staff_member_required
def admin_results(request):
    students = StudentProfile.objects.all()

    if request.method == 'POST':
        student_id = request.POST.get('student')
        semester = int(request.POST.get('semester'))
        subject_code = request.POST.get('subject_code')
        subject_name = request.POST.get('subject_name')
        grade = request.POST.get('grade')
        credits = int(request.POST.get('credits'))

        student = StudentProfile.objects.get(id=student_id)

        Result.objects.create(
            student=student,
            semester=semester,
            subject_code=subject_code,
            subject_name=subject_name,
            grade=grade,
            credits=credits
        )

        return redirect('admin_dashboard')

    return render(request, 'admin/results.html', {
        'students': students
    })

@staff_member_required
def admin_fees(request):
    students = StudentProfile.objects.all()

    if request.method == 'POST':
        student_id = request.POST['student']
        total = request.POST['total_fee']
        paid = request.POST['paid_amount']

        student = StudentProfile.objects.get(id=student_id)

        Fees.objects.update_or_create(
            student=student,
            defaults={
                'total_fee': total,
                'paid_amount': paid
            }
        )

        return redirect('admin_dashboard')

    return render(
        request,
        'admin/fees.html',
        {'students': students}
    )

@staff_member_required
def admin_messages(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        Message.objects.create(
            title=title,
            content=content
        )

        return redirect('admin_dashboard')

    return render(request, 'admin/messages.html')





