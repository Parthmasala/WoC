from urllib import request
from django.shortcuts import render , HttpResponse
from datetime import datetime
from Event_App.models import EventReg,ParticipantReg
import datetime
from django.core.mail import send_mail
from django.conf import settings
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
        email_from = settings.EMAIL_HOST_USER
        receiver = [host_email]
        send_mail(subject, message, email_from , receiver)

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
        return render(request, 'participantReg.html', )

    
def dashboard(request):
    return render(request , 'dashboard.html' )
        
def contact(request):
    return render(request , 'contact.html' )