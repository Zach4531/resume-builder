from django import forms
from .models import Profile, Resume

class ResumeForm(forms.ModelForm):
   class Meta:
       model = Resume
       fields = ['name','summary', 'skills']

