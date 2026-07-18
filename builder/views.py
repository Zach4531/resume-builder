from django.shortcuts import render
from django.http import HttpResponse

from builder.models import About, Certification, Education, Skill, Volunteer, WorkExperience 

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