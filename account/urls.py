from django.urls import path
from .views import loginPage, profile, registerStudent, registerTeacher, logoutUser

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register-teacher/', registerTeacher, name='register-teacher'),
    path('register-student/', registerStudent, name='register-student'),
    path('profile/', profile, name='profile'),
]
