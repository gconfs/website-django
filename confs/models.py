from django.db import models
from django.utils import timezone

from team.models import People as Speaker
import tools.md

from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Conf(models.Model):
    conf_title = models.CharField('Titre', max_length=200)
    conf_description = models.TextField('Description', max_length=100000)
    conf_description_html = models.TextField(editable=False, max_length=120000,
            null=True, default=None, blank=True)
    conf_date = models.DateTimeField('Date', default=timezone.now)
    conf_location = models.CharField('Lieu', max_length=200)
    conf_speakers = models.ManyToManyField(Speaker)
    conf_poster = models.FileField(upload_to='conf/', default=None, null=True,
            blank=True)
    
    class Meta:
        ordering = ['-conf_date']

    def __str__(self):
        return self.conf_title


class TPInfo(models.Model):
    conf = models.ForeignKey(Conf)
    tpinfo_url = models.URLField('URL')
    tpinfo_title = models.CharField('Titre', max_length=200)

    def __str__(self):
        return self.tpinfo_title


class VideoInfo(models.Model):
    conf = models.ForeignKey(Conf)
    videoinfo_url = models.URLField('URL')
    videoinfo_title = models.CharField('Titre', max_length=200)
    youtube_id = models.CharField(max_length=200, editable=False)
    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.videoinfo_url

@receiver(pre_save, sender=Conf)
def descr_md_to_html(sender, **kwargs):
    instance = kwargs['instance']
    instance.conf_description_html = tools.md.markdown_to_html(instance.conf_description)
    print(instance.conf_description_html)


@receiver(pre_save, sender=VideoInfo)
def get_youtube_id(sender, **kwargs):
    instance = kwargs['instance']
    url = instance.videoinfo_url.split('/')[3].split('=')
    url = url[len(url) - 1]
    instance.youtube_id = url.split('?')[0]
