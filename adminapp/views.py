from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def AdminHomePage(request):
    return render(request, 'adminapp/admin_home.html')

from django.shortcuts import redirect
from django.contrib.auth import logout

def AdminLogout(request):
    logout(request)
    return redirect('eventapp:ProjectHomePage')

from django.shortcuts import render, redirect
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        event = request.POST.get('event')
        return HttpResponse(f"Thank you for registering!")
    else:
        event_name = request.GET.get('event', 'Unknown Event')
        return render(request, 'adminapp/registration.html', {'event_name': event_name})


from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import LiveStreamEvent

def live_stream_list(request):
    """List all upcoming live streams."""
    streams = LiveStreamEvent.objects.filter(end_time__gte=now()).order_by('start_time')
    return render(request, 'adminapp/live_stream_list.html', {'streams': streams})

def live_stream_detail(request, stream_id):
    """Display a specific live stream."""
    stream = get_object_or_404(LiveStreamEvent, id=stream_id)
    return render(request, 'adminapp/live_stream_detail.html', {'stream': stream})
