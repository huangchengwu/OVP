from django.contrib import admin
from .models import *
from django.utils.html import format_html


 
from django import forms

# Register your models here.

admin.site.site_title = "在线视频解析后台"
admin.site.site_header = "在线视频解析后台"


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    pass


@admin.register(Tv)
class TvAdmin(admin.ModelAdmin):
    list_display = (
        "Id",
        "name",
        "image_",
        "Tun_",
    )
    search_fields = ("Id", "name")

    def image_(self, obj):
        return format_html(
            '<td class="field-name"><img src="{}" alt="{}" width="100" height="100">',
            obj.imageurl,obj.name,
        )

    image_.short_description = format_html(
        '<th scope="col" class="sortable field-button_"><a href="?o=3">封面图片</a></div><div class="clear"></th></td>'
    )
    image_.allow_tags = True
    def Tun_(self, obj):
        td="<td>"
        print("11",obj.name)
        for i in Server.objects.all():
           td+="<a href=\"%s%s\" target=\"_blank\">%s</a>" %(i.url,obj.url,i.name+"-"+obj.name)


        return format_html(
            td+"</td>",
        )

    Tun_.short_description = format_html(
        '<th scope="col" class="sortable field-button_"><a href="?o=3">通道</a></div><div class="clear"></th></td>'
    )
    Tun_.allow_tags = True
