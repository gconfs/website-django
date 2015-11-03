from django.db import models
from django.utils import timezone

import markdown

from django.db.models.signals import pre_save

from django.dispatch import receiver

# Create your models here.

class Record(models.Model):
    record_date = models.DateField('Date', default=timezone.now)
    record_markdown = models.TextField('Compte rendu (markdown)',
            max_length=100000)
    record_html = models.TextField(editable=False)
    record_is_meeting = models.BooleanField('Réunion', default=True)

@receiver(pre_save, sender=Record)
def makdown_to_html(sender, **kwargs):
    instance = kwargs['instance']
    md = instance.record_markdown
    instance.record_html = markdown.markdown(md,
            extensions=['markdown.extensions.nl2br'])
