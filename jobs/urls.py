from django.urls import path
from .views import JobListView, JobCreateView, JobUpdateView, JobDeleteView, JobDetailView

urlpatterns = [
    path('',JobListView.as_view(),name='dashboard'),
    path('add/',JobCreateView.as_view(),name='add-job'),
    path('update/<int:pk>/', JobUpdateView.as_view(), name='update-job'),
    path('delete/<int:pk>/', JobDeleteView.as_view(), name='delete-job'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
]