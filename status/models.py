from django.db import models
from django.utils import timezone

from team.models import Member

# Create your models here.

class Board(models.Model):
    board_date = models.DateField('Date', default=timezone.now)
    board_year = models.PositiveIntegerField('Année', default=timezone.now().year)
    president = models.OneToOneField(Member, related_name='President_of')
    vice_president = models.OneToOneField(Member,
    related_name='Vice_President_of')
    accountant = models.OneToOneField(Member, related_name='Accountant_of')
    vice_accountant =  models.OneToOneField(Member,
            related_name='Vice_Accountant',default=None, null=True)
    secretary = models.OneToOneField(Member, related_name='Secretary_of')
    vice_secretary = models.OneToOneField(Member,
            related_name='Vice_Secretary_of', default=None, null=True)

    def __str__(self):
        year = self.board_date.year
        return "Bureau de l'année {} - {}".format(year, year + 1)
