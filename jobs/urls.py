from django.urls import path
from .views import JobListView, JobCreateView

urlpatterns = [
    path('',JobListView.as_view(),name='dashboard'),
    path('add/',JobCreateView.as_view(),name='add-job'),
]