from django.db import models
from django.utils import timezone

import re
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
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]'
            '|(?:%[0-9a-fA-F][0-9a-fA-F]))+', md)
    for url in urls:
        md = md.replace(url, '[' + url + '](' + url + ')')
    instance.record_html = markdown.markdown(md,
            extensions=['markdown.extensions.nl2br'])
