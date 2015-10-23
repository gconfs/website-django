from django.db import models
from django.utils import timezone

# Create your models here.

class Conf(models.Model):
    conf_title = models.CharField('Titre', max_length=200)
    conf_description = models.TextField('Description', max_length=1000)
    conf_date = models.DateTimeField('Date', default=timezone.now)
    conf_location = models.CharField('Lieu', max_length=200)

    def __str__(self):
        return self.conf_title

class TPInfo(models.Model):
    conf = models.ForeignKey(Conf)
    tpinfo_url = models.URLField('URL')
    tpinfo_title = models.CharField('Titre', max_length=200)

    def __str__(self):
        return self.tpinfos_title


class VideoInfo(models.Model):
    conf = models.ForeignKey(Conf)
    videoinfo_link = models.URLField('URL')
    videoinfo_title = models.CharField('Titre', max_length=200)

    def __str__(self):
        return self.videoinfo_link
