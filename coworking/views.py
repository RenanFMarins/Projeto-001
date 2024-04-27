from django.http import HttpResponse
from django.shortcuts import render
from utils.coworkings.factory import make_coworking


def home(request):
    return render(request, 'coworking/pages/home.html', context={
        'coworkings': [make_coworking() for _ in range(10)]})


def coworking(request, id):
    return render(request, 'coworking/pages/coworking-view.html', context={
        'coworking': make_coworking(),
        'is_detail_page': True,
    })
