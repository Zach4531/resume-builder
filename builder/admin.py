from django.contrib import admin
from .models import Certification, Education, Profile, Resume, Skill, Volunteer, WorkExperience, JobDuty, VoulunteerDuty

# Register your models here.
admin.site.register(Resume)
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Volunteer)
admin.site.register(JobDuty)
admin.site.register(VoulunteerDuty)