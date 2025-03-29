# Generated by Django 4.2.20 on 2025-03-29 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0008_test_alter_diarylist_brief_alter_essaylist_brief_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='content',
        ),
        migrations.RemoveField(
            model_name='diarylist',
            name='disgusted_count',
        ),
        migrations.RemoveField(
            model_name='diarylist',
            name='encouraged_count',
        ),
        migrations.RemoveField(
            model_name='diarylist',
            name='is_pinned',
        ),
        migrations.RemoveField(
            model_name='diarylist',
            name='is_recommended',
        ),
        migrations.RemoveField(
            model_name='diarylist',
            name='liked_count',
        ),
        migrations.RemoveField(
            model_name='diarylist',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='essay',
            name='content',
        ),
        migrations.RemoveField(
            model_name='essaylist',
            name='disgusted_count',
        ),
        migrations.RemoveField(
            model_name='essaylist',
            name='encouraged_count',
        ),
        migrations.RemoveField(
            model_name='essaylist',
            name='is_pinned',
        ),
        migrations.RemoveField(
            model_name='essaylist',
            name='liked_count',
        ),
        migrations.RemoveField(
            model_name='note',
            name='content',
        ),
        migrations.RemoveField(
            model_name='notelist',
            name='encouraged_count',
        ),
        migrations.AddField(
            model_name='diary',
            name='html_content',
            field=models.TextField(blank=True, null=True, verbose_name='渲染后的HTML'),
        ),
        migrations.AddField(
            model_name='diary',
            name='image_urls',
            field=models.JSONField(blank=True, null=True, verbose_name='插图链接列表'),
        ),
        migrations.AddField(
            model_name='diary',
            name='markdown_content',
            field=models.TextField(blank=True, null=True, verbose_name='渲染前的md'),
        ),
        migrations.AddField(
            model_name='essay',
            name='html_content',
            field=models.TextField(blank=True, null=True, verbose_name='渲染后的HTML'),
        ),
        migrations.AddField(
            model_name='essay',
            name='image_urls',
            field=models.JSONField(blank=True, null=True, verbose_name='插图链接列表'),
        ),
        migrations.AddField(
            model_name='essay',
            name='markdown_content',
            field=models.TextField(blank=True, null=True, verbose_name='渲染前的md'),
        ),
        migrations.AddField(
            model_name='note',
            name='html_content',
            field=models.TextField(blank=True, null=True, verbose_name='渲染后的HTML'),
        ),
        migrations.AddField(
            model_name='note',
            name='image_urls',
            field=models.JSONField(blank=True, null=True, verbose_name='插图链接列表'),
        ),
        migrations.AddField(
            model_name='note',
            name='markdown_content',
            field=models.TextField(blank=True, null=True, verbose_name='渲染前的md'),
        ),
        migrations.AlterField(
            model_name='diarylist',
            name='cover_img',
            field=models.ImageField(blank=True, default='diary_covers', max_length=512, null=True, upload_to='', verbose_name='封面图'),
        ),
        migrations.AlterField(
            model_name='essaylist',
            name='cover_img',
            field=models.ImageField(blank=True, max_length=512, null=True, upload_to='essay_covers', verbose_name='封面图'),
        ),
        migrations.AlterField(
            model_name='notelist',
            name='cover_img',
            field=models.ImageField(blank=True, max_length=512, null=True, upload_to='note_covers', verbose_name='封面图'),
        ),
    ]
