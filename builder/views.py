from django.shortcuts import render
from django.http import HttpResponse

from .models import Education, Profile, Resume, Skill, WorkExperience, Certification
from .forms import ResumeForm

# Create your views here.
def index(request):
    return render(request, 'builder/index.html', {
        'resumes': Resume.objects.all(),
    })

def resume(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    return render(request, 'builder/resume.html', {
        'resume': resume,
        'profile': Profile.objects.first(),
        'education': Education.objects.all(),
    })

def profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'builder/profile.html', {
        'profile': profile,
        'skills': Skill.objects.all(),
        'jobs': WorkExperience.objects.all(),
        'certifications': Certification.objects.all(),

    })