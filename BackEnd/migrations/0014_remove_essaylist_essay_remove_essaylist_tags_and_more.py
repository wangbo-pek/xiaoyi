# Generated by Django 5.1.7 on 2025-03-30 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0013_alter_notelist_cover_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='essaylist',
            name='essay',
        ),
        migrations.RemoveField(
            model_name='essaylist',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Essay',
        ),
        migrations.DeleteModel(
            name='EssayList',
        ),
    ]
