from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.

class Stream(models.Model):
    stream_url = models.URLField()
    stream_title = models.CharField(max_length=200)
    stream_youtube_id = models.CharField(max_length=200, editable=False)

    def __str__(self):
        return self.stream_title

@receiver(pre_save, sender=Stream)
def get_stream_youtube_id(sender, **kwargs):
    instance = kwargs['instance']
    url = instance.stream_url.split('/')[3].split('=')
    url = url[len(url) - 1]
    instance.stream_youtube_id = url.split('?')[0]
    print(instance.stream_youtube_id)
