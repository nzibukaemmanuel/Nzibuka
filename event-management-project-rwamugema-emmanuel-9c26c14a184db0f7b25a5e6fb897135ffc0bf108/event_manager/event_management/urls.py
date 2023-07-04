from django.urls import path
# urls.py

from django.conf import settings
from django.conf.urls.static import static

from .views import create_speaker,speakerlist


urlpatterns = [
    path('createsp', create_speaker, name='createsp'),
    path('speakerlist', speakerlist, name='speakerlist'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
