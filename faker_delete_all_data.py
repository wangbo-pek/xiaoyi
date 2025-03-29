from faker import Faker
from BackEnd import models

faker = Faker('zh_CN')
from django import db
db.connections.close_all()

# 清除旧数据(optional)
def delete_all_faker_data():
    print('正在清除数据')
    models.DiaryList.objects.all().delete()
    models.Diary.objects.all().delete()
    models.EssayList.objects.all().delete()
    models.Essay.objects.all().delete()
    models.NoteList.objects.all().delete()
    models.Note.objects.all().delete()
    models.Tag.objects.all().delete()
    models.SecondClassification.objects.all().delete()
    models.FirstClassification.objects.all().delete()
    print('数据清除完毕')


delete_all_faker_data()