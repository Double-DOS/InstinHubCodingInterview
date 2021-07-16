from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Team, Project, Activity, UserImage
# Create your views here.


def dash_board2(request):
    return HttpResponse('You are here!')


def dash_board(request):
    # fetch all projects from db
    projects = Project.objects.all()

    # fetch the 4 most recent projects
    recentProjects = Project.objects.order_by('-timestamp').all()[:4]

    return render(request, 'dashboard/index.html', context={
        "projects": projects,
        "recent_projects": recentProjects
    })
