from django.contrib import admin
from .models import Conf, VideoInfo, TPInfo, Speaker

# Register your models here.

class TPInfoAdmin(admin.TabularInline):

    model = TPInfo

    extra = 1

    fieldset = [
                (None, {'fields': ['tpinfo_url']}),
                ('Title', {'fields': ['tpinfo_title']}),
                ]

class VideoInfoAdmin(admin.TabularInline):

    model = VideoInfo

    extra = 1

    fieldset = [
                (None, {'fields': ['videoinfo_url']}),
                ('Title', {'fields': ['videoinfo_title']}),
                ]

class ConfAdmin(admin.ModelAdmin):
    fieldset = [
            (None, {'fields': ['conf_title']}),
            ('Date', {'fields': ['conf_date']})
            ]

    inlines = [VideoInfoAdmin, TPInfoAdmin]

    list_display = ['conf_title', 'conf_date', 'conf_location']
    list_filter = ['conf_date']

    search_fields = ['conf_title', 'conf_description']

admin.site.register(Conf, ConfAdmin)
admin.site.register(Speaker)
