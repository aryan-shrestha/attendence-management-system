import json
import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Attendence, Class, classAttendence

# Create your views here.

# renders the index/home page

def home(request):
    return render(request, 'class/index.html')

# renders classes of the teacher that is currently logged in
@login_required(login_url='login')
def classes(request, pk):
    teacher = User.objects.get(id=pk)
    classes = Class.objects.filter(teacher=teacher)

    context = {
        'teacher': teacher,
        'classes': classes
    }

    return render(request, 'class/classes.html', context)

"""
renders attendence of current day 
if attendence is already created it will return the same attendence 
but if the attendence is not created for current day it will create
render out the new attendence. This view also excepts the post method
which marks out the student attendence of the selected class. 
"""
@login_required(login_url='login')
def attendence(request, pk):
    today = datetime.date.today()
    class_obj = Class.objects.get(id=pk)
    today_class_attendence, created = classAttendence.objects.get_or_create(date__year=today.year, date__month=today.month, date__day=today.day, module=class_obj)

    if created:
        students = class_obj.students.all()
        for student in students:
            attendence = Attendence.objects.create(classAttendance=today_class_attendence, 
                                                    student=student, 
                                                    module=class_obj)
        

    student_list = today_class_attendence.attendence_set.all() 

    if request.method == 'POST':
        data = json.loads(request.body)
        attendence = Attendence.objects.get(id=data['studentId'], module__id=data['classId'])

        if attendence.status:
            attendence.status = False
        else:
            attendence.status = True

        attendence.save()
        return JsonResponse("attendence updated", safe=False )

    context = {
        'class': class_obj,
        'class_attendence_detail': today_class_attendence,
        'student_list': student_list,
    }

    return render(request, 'class/attendence.html', context)

# renders the report page
@login_required(login_url='login')
def report(request):
    return render(request, 'class/report.html')

"""
returns weekly/montly attendence as JsonResponse rather rendering or 
passing on context dictionary.

"""

def viewGraph(request, timeframe):

    date = datetime.date.today()

    if timeframe == "week":
        start_week = date - (datetime.timedelta(date.weekday()) + datetime.timedelta(1))
        end_week = start_week + datetime.timedelta(6)
        print("today: ", date)
        print("week start: ", start_week)
        print("week end: ", end_week)
        class_attendences = classAttendence.objects.filter(date__range = [start_week, end_week])\
    
    if timeframe == "month":
        class_attendences = classAttendence.objects.filter(date__year = date.year, date__month = date.month)
            
    data = {}

    for c in class_attendences:
        no_of_present = c.attendence_set.filter(status=True).count()
        data[str(c.date)] = no_of_present


    return JsonResponse(data, safe=False)