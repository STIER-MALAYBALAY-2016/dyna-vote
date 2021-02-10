from django.shortcuts import render, HttpResponse, get_object_or_404
from home.models import *
from django.core.signing import Signer
signer = Signer()

def home(request):
    poll_events = PollEvent.objects.all()
    context = {
        'poll_events':poll_events
    }
    return render(request,"home/home.html",context)

def poll(request,poll_id):
    poll = get_object_or_404(PollEvent, pk=signer.unsign(poll_id))

    context = {
        'poll':poll
    }
    return render(request,'home/poll.html',context)

