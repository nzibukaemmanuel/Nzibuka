from django.shortcuts import render, redirect
from .forms import SpeakerForm
from .models import *

def create_speaker(request):
    if request.method == 'POST':
        form = SpeakerForm(request.POST, request.FILES)
        if form.is_valid():
            speaker = form.save(commit=False)
            speaker.photo = form.cleaned_data['photo']  # Ensure the photo field is properly assigned
            speaker.save()
            return redirect('createsp')
    else:
        form = SpeakerForm()
    return render(request, 'createspeaker.html', {'form': form})


def speakerlist(request):
    speaker = Speaker.objects.all()
    return render(request, 'speakerlist.html', {'speaker': speaker})