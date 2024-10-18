from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, help_text="Correo utilizado para enviar notificaciones")
    description = models.TextField()
    
    def __str__(self):
        return self.title

