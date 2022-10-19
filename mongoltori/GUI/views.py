from django.shortcuts import render

def index(request):
    return render(request, 'GUI/index.html')

def map(request):
    return render(request, 'GUI/map.html')

def science(request):
    return render(request, 'GUI/science.html')
