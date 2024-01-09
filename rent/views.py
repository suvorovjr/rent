from django.shortcuts import render


def index(request):
    return render(request, 'rent/index.html')


def rooms(request):
    return render(request, 'rent/rooms.html')
