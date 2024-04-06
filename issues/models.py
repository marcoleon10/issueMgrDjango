from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import CustomUser  # Importamos el modelo CustomUser

class Issue(models.Model):
    STATUS_CHOICES = (
        ('to_do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    )

    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    )

    summary = models.CharField(max_length=128)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_do')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    reporter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reported_issues')
    assignee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned_issues')  # Modificamos aquí para usar CustomUser
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])
