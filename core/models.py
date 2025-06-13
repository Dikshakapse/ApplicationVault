from django.db import models
from django.conf import settings

class JobApplication(models.Model):
    STATUS_CHOICES=[
        ('applied','Applied'),
        ('interview','Interview'),
        ('offer','Offered'),
        ('reject','Rejected'),
    ]
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_applications')
    company_name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='applied')
    application_date=models.DateField()
    notes=models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.position} at {self.Comapny_name}"
    
