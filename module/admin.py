from django.contrib import admin

from .models import Attendence, Class, classAttendence
# Register your models here.

admin.site.register(Class)
admin.site.register(classAttendence)
admin.site.register(Attendence)