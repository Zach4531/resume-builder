from django.shortcuts import render
from django.http import HttpResponse

from builder.models import About, Certification, Education, Skill, Volunteer, WorkExperience , Resume

# Create your views here.
def index(request):
    return render(request, 'builder/index.html', {
        'resumes': Resume.objects.all(),
    })

def resume(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    return render(request, 'builder/resume.html', {
        'resume': resume,
        'about': About.objects.first(),
        'education': Education.objects.all(),
    })