from urllib import request
from django.shortcuts import render , HttpResponse
from datetime import datetime
from Event_App.models import EventReg
import datetime
from django.contrib.admin.widgets import AdminSplitDateTime, AdminDateWidget, AdminTimeWidget

# Create your views here.
def index(request):
    # return HttpResponse("Hello")
    # refer = {
    #     'variable' : "check for variable"
    # }
    return render(request , 'index.html')

def eventReg(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        description = request.POST.get('description')
        location = request.POST.get('location')
        poster_link = request.POST.get('poster_link')
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        registration_deadline = request.POST.get('registration_deadline')
        host_email = request.POST.get('host_email')
        host_password = request.POST.get('host_password')
        event_detail = EventReg(
            event_name=event_name,
            description=description,
            location=location,
            poster_link=poster_link,
            date_from=date_from,
            date_to=date_to,
            registration_deadline=registration_deadline,
            host_email=host_email,
            host_password=host_password,
            )
        event_detail.save()
        # subject = 'Information of Registered Event'
        # message = "Event - " + event_name + "\n Description :" + description + "\nLocation : " + location
        # + "\nFrom: " + date_from + " to " + date_to 
        # + "\nRegistration Deadline : " + registration_deadline 
        # +"\nPoster for event : " + poster_link
        # +"\nHost email id : " + host_email + " and Password : " + host_password 
        # +"\nThank you."
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [host_email,]
        # send_mail(subject, message, email_from, recipient_list)

    return render(request , 'eventReg.html' )
    
def participantReg(request):
    if request.method == 'GET':
        date_time = datetime.datetime.now()
        info = {
            'date_time' : date_time,
            'event_info' : EventReg.objects.all()
        }
        return render(request, 'participantReg.html', info)
    elif request.method == 'POST':
        return render(request, 'participantReg.html', )

    
def dashboard(request):
    return render(request , 'dashboard.html' )
        
def contact(request):
    return render(request , 'contact.html' )