from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
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

class JobUpdateView(UpdateView):
    model = JobApplication
    template_name = 'job_form.html'
    fields = ['company', 'position', 'url', 'status', 'notes']
    success_url = reverse_lazy('dashboard')

class JobDeleteView(DeleteView):
    model = JobApplication
    template_name = 'job_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

class JobDetailView(DetailView):
    model = JobApplication
    template_name = 'job_detail.html'
    context_object_name = 'job'