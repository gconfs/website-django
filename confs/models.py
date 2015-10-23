from django.db import models
from django.utils import timezone

# Create your models here.

class Speaker(models.Model):
    speaker_name = models.CharField('Nom', max_length=200)
    speaker_firstname = models.CharField('Prénom', max_length=200,
            default=None, null=True)
    speaker_pseudo = models.CharField('Pseudo', max_length=200,
            default=None, null=True)
    speaker_website = models.URLField('Website', max_length=200, default=None, null=True)
    
    def __str__(self):
        return self.speaker_firstname + (' ' if self.speaker_pseudo
                else (' \"' + self.speaker_pseudo + '\" ')) + self.speaker_name


class Conf(models.Model):
    conf_title = models.CharField('Titre', max_length=200)
    conf_description = models.TextField('Description', max_length=2048)
    conf_date = models.DateTimeField('Date', default=timezone.now)
    conf_location = models.CharField('Lieu', max_length=200)
    conf_speakers = models.ManyToManyField(Speaker)
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

    def __str__(self):
        return self.videoinfo_url
