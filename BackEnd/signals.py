from django.db.models.signals import post_save
from django.dispatch import receiver
from BackEnd import models


# 信号：监听Note被创建时，自动创建与之相关联的info
@receiver(post_save, sender=models.Note, dispatch_uid='create_info_for_note')
def create_info(sender, instance, created, **kwargs):
    if created:
        models.NoteInfo.objects.create(note=instance)


# 信号：监听Essay被创建时，自动创建与之相关联的info
@receiver(post_save, sender=models.Essay, dispatch_uid='create_info_for_essay')
def create_info(sender, instance, created, **kwargs):
    if created:
        models.EssayInfo.objects.create(essay=instance)
