from unicodedata import name
from django.urls import path
from .views import attendence, classes, home, report, viewGraph

urlpatterns = [
    path('', home, name='home'),
    path('classes/<int:pk>', classes, name='classes'),
    path('attendence/<int:pk>', attendence, name='attendence'),
    path('report/', report, name='report'),
    path('show_chart/<str:timeframe>/',  viewGraph, name='show-chart')
]
