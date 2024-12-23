# Generated by Django 3.2.1 on 2024-12-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='通道1', max_length=255, unique=True, verbose_name='解析通道名')),
                ('url', models.CharField(default='http://jiexi44.qmbo.cn/jiexi/?url=', max_length=255, unique=True, verbose_name='连接')),
            ],
            options={
                'verbose_name': '解析服务配置',
                'verbose_name_plural': '解析服务配置',
            },
        ),
        migrations.CreateModel(
            name='Tv',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='通道1', max_length=255, unique=True, verbose_name='解析通道名')),
                ('tvt_type', models.CharField(choices=[('动漫', '动漫'), ('美剧', '美剧'), ('国产电视剧', '国产电视剧')], max_length=20, verbose_name='电视类型')),
                ('imageurl', models.CharField(default='https://img0.baidu.com/it/u=3888892748,4130106922&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=700', max_length=255, unique=True, verbose_name='封面图片')),
                ('url', models.CharField(default='https://v.qq.com/x/cover/mzc00200xf3rir6/n00468uwo0m.html', max_length=255, unique=True, verbose_name='连接')),
            ],
            options={
                'verbose_name': '电视配置',
                'verbose_name_plural': '电视配置',
            },
        ),
    ]