from django.shortcuts import render
from .models import Profile
from skills.models import Skill, Project
# Create your views here.
def home(request):
    profile = Profile.objects.all()
    skill = Skill.objects.all()
    project = Project.objects.all()
    context = {
        'profile':profile, 
        'skill': skill,
        'project': project
    }
    return render(request, 'home.html', context)


def about_me(request):
    profile = Profile.objects.only('about')
    return render(request, 'about.html', {'profile':profile})


def contact(request):
    return render(request, 'contact.html')