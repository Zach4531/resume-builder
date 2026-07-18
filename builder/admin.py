from django.contrib import admin

from .models import About, Certification, Education, Skill, Volunteer, WorkExperience, JobDuty, VoulunteerDuty

# Register your models here.
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Volunteer)
admin.site.register(JobDuty)
admin.site.register(VoulunteerDuty)