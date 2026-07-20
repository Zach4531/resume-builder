from django.db import models


MONTH_CHOICES = [
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
]

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Resume(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField('Skill', related_name='skills', blank=True)
    jobs = models.ManyToManyField('WorkExperience', related_name='jobs', blank=True)
    volunteer_experiences = models.ManyToManyField('Volunteer', related_name='volunteer_experiences', blank=True)
    certifications = models.ManyToManyField('Certification', related_name='certifications', blank=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    github = models.URLField(blank=True, null=True)
    cpen = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
     
    
class WorkExperience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    start_year = models.IntegerField(default=0)
    end_month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    end_year = models.IntegerField(default=0)
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.position} at {self.company}"
    
class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.degree} at {self.institution}"   
    
class Certification(models.Model):
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} from {self.institution}"
    
class Volunteer(models.Model):
    organization = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    start_year = models.IntegerField()
    end_month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    end_year = models.IntegerField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.role} at {self.organization}"
    
class JobDuty(models.Model):
    job = models.ForeignKey(WorkExperience, on_delete=models.CASCADE, related_name='job_duties')
    description = models.TextField()

    def __str__(self):
        return f"Duty for {self.job.position} at {self.job.company}"

class VoulunteerDuty(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name='volunteer_duties')
    description = models.TextField()

    def __str__(self):
        return f"Duty for {self.volunteer.role} at {self.volunteer.organization}"
