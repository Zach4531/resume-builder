from django.shortcuts import render
from django.http import HttpResponse

from builder.models import Education, Profile, Resume

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