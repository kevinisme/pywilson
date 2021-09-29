from django.shortcuts import render


def index(request):
    return render(request, 'index0.html')