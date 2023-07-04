from django.urls import path
from .views import create_speaker, speaker_list

app_name = 'event_management'

urlpatterns = [
    path('create_speaker/', create_speaker, name='create_speaker'),
    path('speaker_list', speaker_list, name='speaker_list'),
]
