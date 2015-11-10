from django.db import models
from django.utils import timezone

import tools.md

from django.core.mail import send_mail
from django.db.models.signals import pre_save

from gconfs_website import settings

from django.dispatch import receiver

# Create your models here.

class Record(models.Model):
    record_date = models.DateField('Date', default=timezone.now)
    record_markdown = models.TextField('Compte rendu (markdown)',
            max_length=100000)
    record_html = models.TextField(editable=False)
    record_is_meeting = models.BooleanField('Réunion', default=True)
    record_sent = models.BooleanField('Envoyer', default=False)

    def __str__(self):
        s = "la réunion" if self.record_is_meeting else "l'Assemblée Générale"
        return "Compte rendu de {} du {}".format(s, self.record_date)

@receiver(pre_save, sender=Record)
def process_record(sender, **kwargs):
    instance = kwargs['instance']
    md = instance.record_markdown
    if instance.record_sent:
        recipients = [settings.CR_EMAIL]
        send_mail(settings.EMAIL_STD_PREFIX + ' CR : Réunion du ' +
                str(instance.record_date),
                settings.CR_MESSAGE_START.format(instance.record_date) + md +
                settings.CR_MESSAGE_END, settings.CR_EMAIL,
                recipients)
        instance.record_sent = False
    instance.record_html = tools.md.markdown_to_html(md)
