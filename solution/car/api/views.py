from django.shortcuts import render

from .models import Car


def list_trips(request):
    trips = Car.objects.all()
    return render(request, 'trips.html', {'trips': trips})


def trip(request):
    ...