from django.db import models

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('APPLIED', 'Applied'),
        ('INTERVIEW', 'Interviewing'),
        ('OFFER', 'Offer Received'),
        ('REJECTED', 'Rejected'),
    ]

    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    date_applied = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default='APPLIED')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company} - {self.position}"
