# College Management System (Django)

A College Management System built using **Django**, **SQLite**, **HTML**, and **CSS**.  
This project follows Django best practices and is designed for beginners, academic use, and interview preparation.

---

## Features

### User Roles
- Admin
- Student

---

## Student Module

### Authentication
- Student login using Register Number and Password

### Dashboard Pages
- Profile
- Attendance
- Semester Results
- Fees Structure
- Messages
- Logout

### Student Functionalities
- View personal profile details
- View semester-wise attendance (read-only)
- View semester results with CGPA
- View fee details (total, paid, due)
- Read announcements sent by admin

---

## Admin Module

- Admin login and dashboard
- Add and manage student profiles
- Add, update, and view attendance records
- Add, update, and view semester results
- Manage fees structure
- Send announcements to all students

---

## Tech Stack

- Backend: Django (Python)
- Database: SQLite
- Frontend: HTML, CSS
- Authentication: Django Auth (Role-Based)
- Editor: Visual Studio Code

---

## Project Structure

college_cms/
├── college_cms/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── accounts/
├── student/
├── admin_panel/
│
├── templates/
│ ├── auth/
│ ├── student/
│ └── admin/
│
├── static/
│ └── css/
│
├── manage.py
└── README.md


---

## HTML & CSS Integration

- All HTML files are placed inside the `templates/` directory
- CSS files are stored in the `static/css/` directory
- Django template tags are used to render dynamic data
- No Bootstrap or external UI libraries are used

---

## Responsive Design

- Built using pure CSS
- Uses Flexbox and media queries
- Mobile-friendly layout without frameworks

---

## Security

- Django authentication enabled
- Role-based access control
- Students can view only their own data
- Admin has full access to manage records

---


---

## Screenshots

> Add screenshots inside a  folder in the root directory.

### Student Module
- Student Login Page  
  <img width="1918" height="924" alt="Screenshot 2025-12-22 182242" src="https://github.com/user-attachments/assets/cc94279a-261b-4a19-b1f1-e9b0c2ebea96" />
`
- Student Dashboard  

  <img width="1882" height="867" alt="Screenshot 2025-12-22 182321" src="https://github.com/user-attachments/assets/26d7df18-3b07-4aed-b3a7-4fca6d3f6d52" />

- Attendance Page  
  <img width="1854" height="885" alt="Screenshot 2025-12-22 182335" src="https://github.com/user-attachments/assets/6d0ff022-e1b2-43e9-984c-a36c4cdfe622" />

- Semester Results Page  
  <img width="1907" height="801" alt="Screenshot 2025-12-22 182401" src="https://github.com/user-attachments/assets/77c24334-e821-4dd4-a71a-5b53f2e65fd9" />

- Fees Structure Page  
   <img width="1816" height="744" alt="Screenshot 2026-01-12 120101" src="https://github.com/user-attachments/assets/68997a7c-cfb1-42cc-84f0-aa3915826d35" />

- Messages Page  
  <img width="1918" height="918" alt="Screenshot 2025-12-22 182429" src="https://github.com/user-attachments/assets/1ded2ee2-35db-47b2-a53a-f4815f4ff418" />


### Admin Module
- Admin Login  
  `screenshots/admin_login.png`
- Admin Dashboard  
  `screenshots/admin_dashboard.png`
- Manage Students  
  `screenshots/manage_students.png`
- Attendance Management  
  `screenshots/admin_attendance.png`
- Results Management  
  `screenshots/admin_results.png`

Example usage:

  <img width="1914" height="913" alt="Screenshot 2025-12-22 182310" src="https://github.com/user-attachments/assets/eeabf977-b52f-4cdf-9c62-6cc078d9fcb0" />

