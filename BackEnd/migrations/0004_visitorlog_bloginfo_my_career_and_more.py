# Generated by Django 5.1.7 on 2025-04-07 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0003_bloginfo_coffee_alipay_bloginfo_coffee_wechat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(db_index=True, max_length=64, verbose_name='访客唯一标识')),
                ('ip_addr', models.GenericIPAddressField()),
                ('user_agent', models.TextField()),
                ('referer', models.TextField(blank=True, null=True)),
                ('path', models.CharField(max_length=255, verbose_name='访问路径')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='my_career',
            field=models.CharField(default='产品经理', max_length=32, verbose_name='我的职业'),
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='my_formal_intro',
            field=models.CharField(default='', max_length=256, verbose_name='我的介绍'),
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='my_location',
            field=models.CharField(default='北京', max_length=32, verbose_name='我的所在地'),
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='my_motto',
            field=models.CharField(default='', max_length=128, verbose_name='我的座右铭'),
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='my_short_intro',
            field=models.CharField(default='', max_length=64, verbose_name='我的简短介绍'),
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='my_wisdom',
            field=models.CharField(default='', max_length=256, verbose_name='我的警示名言'),
        ),
    ]
