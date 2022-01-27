from email import message
from pyexpat.errors import messages
from tabnanny import check
from urllib import request
from django.shortcuts import render , HttpResponse
from datetime import datetime
from Event_App.models import EventReg,ParticipantReg,ContactReg
import datetime,time,os
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.admin.widgets import AdminSplitDateTime, AdminDateWidget, AdminTimeWidget
from twilio.rest import Client

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

        date_time = datetime.datetime.now()
        date_time = str(date_time)
        if request.POST.get('date_from') < date_time:
            check=0
        elif request.POST.get('registration_deadline') < date_time:
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
            # email_from = settings.EMAIL_HOST_USER
            # email_to = [host_email]
            # subject = 'Information of Registered Event'
            # message = "Event - " + event_name \
            # + "\n" + "Description : " + description \
            # + "\n" +  "Location : " + location \
            # + "\n" + "From: " + date_from + " to " + date_to \
            # + "\n" +  "Registration Deadline : " + registration_deadline \
            # + "\n" + "Poster for event : " + poster_link \
            # + "\n" + "Event ID : " + str(event_detail.id) \
            # + "\n" + "Your login Password : " + host_password \
            # + "\n" + "\n" + "Thank you." + "\n" + "Parth Managment"
            # send_mail(subject, message, email_from , email_to)
    return render(request , 'eventReg.html' )
    
def participantReg(request):
    if request.method == 'GET':
        date_time = datetime.datetime.now()
        detail = {
            'date_time' : date_time,
            'event_detail' : EventReg.objects.all()
        }
        return render(request, 'participantReg.html', detail)
    elif request.method == 'POST':
        participant_detail = ParticipantReg.objects.all()
        check=1
        for participant in participant_detail:
            old_participant_email = participant.participant_email
            if old_participant_email == request.POST.get('participant_email') :
                if participant.selected_event_id == int(request.POST.get('select_event')) :
                    check=0
                    break

        if check == 0:
            messages.warning(request, "You are already registered for this event.Please try with other Email id.")
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

            # email_from = settings.EMAIL_HOST_USER
            # email_to = [participant_email]
            # subject = 'Participating Event Information'
            # message = "Hello " + participant_name \
            #         + "\n" + "You have registered for event - " + selected_event_name \
            #         + "\n" + "Your ID : " + str(participant_detail.id) \
            #         + "\n" + "Enail ID : " + participant_email \
            #         + "\n" + "Event Details :- " \
            #         + "\n" + "Description : " + event_by_id.description \
            #         + "\n" +  "Location : " + event_by_id.location \
            #         + "\n" +  "Poster link : " + event_by_id.poster_link \
            #         + "\n" + "From: " + str(event_by_id.date_from) + " to " + str(event_by_id.date_to) \
            #         + "\n" + "Registration Type : " + registration_type \
            #         + "\n" + "Booked for - " + num_of_people + " people" \
            #         + "\n" + "\n" + "Thank you." + "\n" + "Parth Managment"
            # send_mail(subject, message, email_from , email_to)

            # account_sid = ''
            # auth_token = ''
            # client = Client(account_sid, auth_token)

            # client.messages.create(
            #                     body= "\n" + "\n" + "Hello " + participant_name \
            #                     + "\n" + "You have registered for event - " + selected_event_name \
            #                     + "\n" + "Your ID : " + str(participant_detail.id) \
            #                     + "\n" + "Enail ID : " + participant_email \
            #                     + "\n" + "Event Details :- " \
            #                     + "\n" + "Description : " + event_by_id.description \
            #                     + "\n" +  "Location : " + event_by_id.location \
            #                     + "\n" +  "Poster link : " + event_by_id.poster_link \
            #                     + "\n" + "From: " + str(event_by_id.date_from) + " to " + str(event_by_id.date_to) \
            #                     + "\n" + "Registration Type : " + registration_type \
            #                     + "\n" + "Booked for - " + num_of_people + " people" \
            #                     + "\n" + "\n" + "Thank you." + "\n" + "Parth Managment",
            #                     from_='+16072846013',
            #                     to='+91' + participant_contact
            #                 )
            #
            messages.success(request, 'Thank You! for registering in the event')
            return render(request, 'participantReg.html' )

    
def dashboard(request):
    # if request.method == 'GET':
    #     return render(request, 'dashboard.html')
    if request.method == 'POST':
        event_detail = EventReg.objects.all()
        check = 0
        for event in event_detail:
            if str(event.id) == str(request.POST.get('event_id')):
                if str(event.host_email) == str(request.POST.get('dashboard_email')):
                    if str(event.host_password) == str(request.POST.get('dashboard_password')):
                        check = 1
                        break

        if check == 0 :
            messages.error(request, "Please enter proper ID , Email and Password!")
            return render(request , 'dashboard.html' )
        elif check == 1:
            try:
                participant_detail = ParticipantReg.objects.filter(selected_event_id=request.POST.get('event_id'))
            except ParticipantReg.DoesNotExist:
                participant_detail = None
            
            detail = {
                'participant_detail' : participant_detail
            }
            return render(request, 'dashboard.html', detail)
    return render(request , 'dashboard.html' )
        
def contact(request):
    if request.method == 'POST':
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_description = request.POST.get('contact_description')
        query_detail = ContactReg(
            contact_name = contact_name,
            contact_email=contact_email,
            contact_description=contact_description,
            )
        query_detail.save()
        messages.success(request, 'Thank You for your support! We will get back to you.')
        # email_from = settings.EMAIL_HOST_USER
        # email_to = [contact_email]
        # subject = 'Query is under process'
        # message = "Dear " + contact_name + " , "\
        # + "\n" + "Thank You for writing to us.And we will try to get back to you as soon as possible." \
        # + "\n" + "\n" + "Thank you." + "\n" + "Parth Managment"
        # send_mail(subject, message, email_from , email_to)
    return render(request , 'contact.html' )