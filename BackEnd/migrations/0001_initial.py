# Generated by Django 5.1.7 on 2025-04-05 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=16, verbose_name='分类')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('markdown_content', models.TextField(blank=True, null=True, verbose_name='渲染前的md')),
                ('image_urls', models.JSONField(blank=True, null=True, verbose_name='插图链接列表')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('markdown_content', models.TextField(blank=True, null=True, verbose_name='渲染前的md')),
                ('image_urls', models.JSONField(blank=True, null=True, verbose_name='插图链接列表')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True, verbose_name='标签名称')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='DiaryList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('brief', models.CharField(blank=True, max_length=128, null=True, verbose_name='摘要')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('cover_img', models.URLField(blank=True, max_length=512, null=True, verbose_name='封面图')),
                ('diary', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.diary')),
            ],
        ),
        migrations.CreateModel(
            name='NoteList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('brief', models.CharField(blank=True, max_length=128, null=True, verbose_name='摘要')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('viewed_count', models.IntegerField(default=0, verbose_name='被浏览次数')),
                ('liked_count', models.IntegerField(default=0, verbose_name='被赞次数')),
                ('disgusted_count', models.IntegerField(default=0, verbose_name='被踩次数')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_pinned', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('is_recommended', models.BooleanField(default=False, verbose_name='是否推荐')),
                ('cover_img', models.URLField(blank=True, max_length=512, null=True, verbose_name='封面图')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.category')),
                ('note', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.note')),
                ('tags', models.ManyToManyField(to='BackEnd.tag')),
            ],
        ),
    ]
