from django.db import models



# Create your models here.
class Server(models.Model):
    Id = models.AutoField(primary_key=True)

    name = models.CharField(
        max_length=255, verbose_name="解析通道名", default="通道1", unique=True
    )
    url = models.CharField(
        max_length=255,
        verbose_name="连接",
        default="http://jiexi44.qmbo.cn/jiexi/?url=",
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "解析服务配置"
        verbose_name_plural = verbose_name


class Tv(models.Model):
    Id = models.AutoField(primary_key=True)

    name = models.CharField(
        max_length=255, verbose_name="片名", default="斗罗大陆", unique=True
    )
    TVT_CHOICES = [
        ('动漫', '动漫'),
        ('美剧', '美剧'),
        ('国产电视剧', '国产电视剧'),
    ]

  
    tvt_type = models.CharField( verbose_name="电视类型",max_length=20,default=0, choices=TVT_CHOICES)


    imageurl = models.CharField(
        max_length=255,
        verbose_name="封面图片",
        default="https://img0.baidu.com/it/u=3888892748,4130106922&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=700",
        unique=True,
    )
    url = models.CharField(
        max_length=255,
        verbose_name="连接",
        default="https://v.qq.com/x/cover/mzc00200xf3rir6/n00468uwo0m.html",
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "电视配置"
        verbose_name_plural = verbose_name
