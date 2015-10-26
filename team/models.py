from django.db import models
from django.utils import timezone

# Create your models here.

class Member(models.Model):
    member_name = models.CharField('Nom', max_length=200)
    member_firstname = models.CharField('Prénom', max_length=200,
            default=None, null=True, blank=True)
    member_pseudo = models.CharField('Pseudo', max_length=200,
            default=None, null=True, blank=True)
    member_website = models.URLField('Website', max_length=200, default=None,
            null=True, blank=True)
    
    def __str__(self):
        return self.member_firstname + (' ' if not self.member_pseudo
                else (' \"' + self.member_pseudo + '\" ')) + self.member_name
