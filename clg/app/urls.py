from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path('about',views.about),
    path('contact',views.contact),
    path('course',views.course),
    path('course1',views.course1),
    path('course2',views.course2),
    path('course3',views.course3),
    path('course4',views.course4),
    path('course5',views.course5),
    path('thanks',views.thanks),
]