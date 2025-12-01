from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import JobApplication
from django.urls import reverse_lazy

class JobListView(ListView):
    model = JobApplication
    template_name = 'job_list.html'
    context_object_name = 'jobs'

class JobCreateView(CreateView):
    model = JobApplication
    template_name = 'job_form.html'
    fields = ['company', 'position', 'url', 'status', 'notes']
    success_url = reverse_lazy('dashboard')