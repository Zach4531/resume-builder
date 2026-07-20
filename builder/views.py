from django.shortcuts import render
from django.http import HttpResponse

from builder.models import About, Certification, Education, Skill, Volunteer, WorkExperience , Resume

# Create your views here.
def index(request):
    return render(request, 'builder/index.html', {
        'about': About.objects.first(),
        'skills': Skill.objects.all(),
        'certifications': Certification.objects.all(),
        'education': Education.objects.all(),
        'volunteer': Volunteer.objects.all(),
        'work_experience': WorkExperience.objects.all()
    })

def resume(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    return render(request, 'builder/resume.html', {
        'resume': resume,
        'about': About.objects.first(),
        'education': Education.objects.all(),
    })