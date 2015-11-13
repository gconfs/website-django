from django.db import models
from django.utils import timezone

# Create your models here.

class People(models.Model):
    people_name = models.CharField('Nom', max_length=200)
    people_firstname = models.CharField('Prénom', max_length=200,
            default=None, null=True, blank=True)
    people_pseudo = models.CharField('Pseudo', max_length=200,
            default=None, null=True, blank=True)
    people_email = models.EmailField('Mail', max_length=500, default=None,
            null=True, blank=True)
    people_membership = models.BooleanField('Membre', default=True)
    
    class Meta:
        ordering = ['people_name', 'people_firstname']
        verbose_name_plural = "People"
    
    def __str__(self):
        return self.people_firstname + (' ' if not self.people_pseudo
                else (' \"' + self.people_pseudo + '\" ')) + self.people_name
