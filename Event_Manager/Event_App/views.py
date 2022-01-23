from email import message
from pyexpat.errors import messages
from urllib import request
from django.shortcuts import render , HttpResponse
from datetime import datetime
from Event_App.models import EventReg,ParticipantReg
import datetime,time
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.admin.widgets import AdminSplitDateTime, AdminDateWidget, AdminTimeWidget

# Create your views here.
def index(request):
    # return HttpResponse("Hello")
    # refer = {
    #     'variable1' : "check for variable"
    #     'variable2' : "dvd fdv d  vdv"
    # }
    # return render(request , 'index.html' , refer)
    return render(request , 'index.html')

def eventReg(request):
    if request.method == 'POST':
        check=1
        if request.POST.get('date_from') > request.POST.get('date_to'):
            check=0
        elif request.POST.get('date_from') < request.POST.get('registration_deadline'):
            check=0

        if check == 0:
            messages.warning(request, "Please enter proper date and time.")
            return render(request , 'eventReg.html' )
        elif check == 1 :
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
            messages.success(request, 'Your Event has been Registered.Thank You!')
            email_from = settings.EMAIL_HOST_USER
            email_to = [host_email]
            subject = 'Information of Registered Event'
            message = "Event - " + event_name \
            + "\n" + "Description : " + description \
            + "\n" +  "Location : " + location \
            + "\n" + "From: " + date_from + " to " + date_to \
            + "\n" +  "Registration Deadline : " + registration_deadline \
            + "\n" + "Poster for event : " + poster_link \
            + "\n" + "Event ID : " + str(event_detail.id) \
            + "\n" + "Your login Password : " + host_password \
            + "\n" + "\n" + "Thank you." + "\n" + "Parth Managment"
            send_mail(subject, message, email_from , email_to)
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
        participant_info = ParticipantReg.objects.all()
        check=1
        for participant in participant_info:
            old_participant_email = participant.participant_email
            if old_participant_email == request.POST.get('participant_email') :
                if participant.selected_event_id == int(request.POST.get('select_event')) :
                    check=0
                    messages.warning(request, "You are already registered for this event.Please try with other Email id.")
                    break

        if check == 0:
             return render(request , 'participantReg.html' )
        elif check == 1 :
            participant_name = request.POST.get('participant_name')
            participant_contact = request.POST.get('participant_contact')
            participant_email = request.POST.get('participant_email')
            selected_event_id = request.POST.get('select_event')
            registration_type = request.POST.get('registration_type')
            num_of_people = request.POST.get('num_of_people')
            
            event_by_id = EventReg.objects.get(id=selected_event_id)
            selected_event_name = event_by_id.event_name
            participant_detail = ParticipantReg(
                participant_name = participant_name,
                participant_contact = participant_contact,
                participant_email = participant_email,
                selected_event_id = selected_event_id,
                selected_event_name = selected_event_name,
                registration_type = registration_type,
                num_of_people = num_of_people,
            )
            participant_detail.save()
            return render(request, 'participantReg.html' )

    
def dashboard(request):
    return render(request , 'dashboard.html' )
        
def contact(request):
    return render(request , 'contact.html' )