from django.shortcuts import render
from .models import Project
from portfolio import views


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
