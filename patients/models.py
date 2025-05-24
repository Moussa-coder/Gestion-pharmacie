from django.db import models
from owners.models import Owner
# Create your models here.
class Patient(models.Model):
    ANIMAL_TYPES= [
        ('chat', 'Chat'),
        ('chien', 'Chien'),
        ('lapin', 'Lapin'),
    ]
    
    SEX_CHOICES = [
        ('M', 'Mâle'),
        ('F', 'Femelle',)
    ]
    
    name = models.CharField(max_length=100)
    animal_type = models.CharField(max_length=10, choices=ANIMAL_TYPES)
    breed = models.CharField(max_length=100)
    birth_date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='patients')
    
    def __str__(self):
        return f"{self.name} ({self.animal_type})"