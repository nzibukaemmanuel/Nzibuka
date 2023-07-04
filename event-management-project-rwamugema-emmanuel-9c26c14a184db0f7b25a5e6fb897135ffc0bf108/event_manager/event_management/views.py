from django.shortcuts import render, redirect
from .models import Speaker
from .forms import SpeakerForm

def create_speaker(request):
    if request.method == 'POST':
        form = SpeakerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
            return redirect('event_management:speaker_list')
    else:
        form = SpeakerForm()
    return render(request, 'createspeaker.html', {'form': form})

def speaker_list(request):
    speakers = Speaker.objects.all()
    return render(request, 'event_management/speaker_list.html', {'speakers': speakers})
