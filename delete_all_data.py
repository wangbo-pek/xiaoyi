from faker import Faker

faker = Faker('zh_CN')

# 清除旧数据
def delete_all_faker_data():
    from BackEnd import models
    print('正在清除数据')
    models.DiaryList.objects.all().delete()
    models.Diary.objects.all().delete()
    models.NoteList.objects.all().delete()
    models.Note.objects.all().delete()
    models.Tag.objects.all().delete()
    models.Category.objects.all().delete()
    print('✅ 数据清除完毕')

delete_all_faker_data()