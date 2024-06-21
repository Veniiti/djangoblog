from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

# urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Twoje URL-e aplikacji
]

# Dodaj poniższe linie tylko w trybie DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
