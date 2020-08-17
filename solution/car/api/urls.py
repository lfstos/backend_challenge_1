from django.urls import path

from .views import trip, list_trips

urlpatterns = [
    path('', list_trips, name='list_trips'),
    path('new_trip', trip, name='new_trip'),
]
