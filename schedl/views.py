
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Event, Participant, User
from django.db.models import Q
from django.utils.dateparse import parse_time
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def schedu(request):        
    if request.method == 'POST':
        # Assuming the POST data has all the necessary fields
        host_id = request.POST.get('id')
        name = request.POST.get('event')
        event_date = request.POST.get('date')
        event_time = request.POST.get('time')
        details = request.POST.get('dets')
        try:
            host = User.objects.get(pk=host_id)
        except User.DoesNotExist:
            return HttpResponse("User does not exist.", status=404) 
        
        # Create and save the new event
        new_event = Event(
            name=name,
            event_date=event_date,
            event_time=event_time,
            details=details,
            host = host
        )
        new_event.save()
    
    return render(request, 'schedule.html')

def upcoming(request):
    if request.method == 'POST':
        email_id = request.POST.get('email_id')
        event_id = request.POST.get('event_id')
        
        # Get the event object
        event = Event.objects.get(pk=event_id)
        
        # Create the participant if not exists
        Participant.objects.get_or_create(event=event, email_id=email_id)
    
    # Fetch all upcoming events
    events = Event.objects.filter(event_date__gte=datetime.now().date(), event_time__gte=datetime.now().time()).order_by('event_date')
    
    data = []
    for event in events:
        registered_count = Participant.objects.filter(event=event).count()
        data.append({
            "id": event.event_id,
            "name": event.name,
            "date": event.event_date,
            "time": event.event_time.strftime("%I:%M %p"),
            "host": event.host.name,
            "registered": registered_count,
            "details": event.details,
        })

    context = {"data": data}
    return render(request, "upcoming.html", context)

def past(request):
    # Fetch all past events
    events = Event.objects.filter(
    Q(event_date__lt=datetime.now().date()) |  # Events before today
    Q(event_date=datetime.now().date(), event_time__lt=datetime.now().time())  # Events today but before current time
).order_by('-event_date', '-event_time')
    data = []
    for event in events:
        data.append({
            "id": event.event_id,
            "name": event.name,
            "date": event.event_date,
            "time": event.event_time.strftime("%I:%M %p"),
            "host": event.host.name,
            "details": event.details,
        })

    context = {"data": data}
    return render(request, "past.html", context)

def get_list_based_on_id(request, item_id):
    # Get participants of the specific event
    participants = Participant.objects.filter(event_id=item_id).values_list('email_id', flat=True)
    
    return JsonResponse({'data_list': list(participants)})
