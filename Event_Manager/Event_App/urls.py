from django.contrib import admin
from django.urls import path
from Event_App import views

urlpatterns = [
    path('', views.index , name='App'),
    path('eventReg', views.eventReg , name='eventReg'),
    path('participantReg', views.participantReg , name='participantReg'),
    path('dashboard', views.dashboard , name='dashboard'),
    path('contact', views.contact , name='contact'),
]
