from django.shortcuts import render
from django.views.generic import ListView
from .models import JobApplication

class JobListView(ListView):
    model = JobApplication
    template_name = 'job_list.html'
    context_object_name = 'jobs'
