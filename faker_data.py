from faker import Faker
import random
from BackEnd import models
from BackEnd.services import note_service, essay_service, diary_service

print('faker开始生产数据')
# 实例化Faker，生产中文数据
faker = Faker('zh_CN')

# 清除旧数据(optional)
def delete_all_faker_data():
    print('正在清除数据')
    models.DiaryList.objects.all().delete()
    models.DiaryInfo.objects.all().delete()
    models.Diary.objects.all().delete()
    models.EssayList.objects.all().delete()
    models.EssayInfo.objects.all().delete()
    models.Essay.objects.all().delete()
    models.NoteList.objects.all().delete()
    models.NoteInfo.objects.all().delete()
    models.Note.objects.all().delete()
    models.Tag.objects.all().delete()
    models.SecondClassification.objects.all().delete()
    models.FirstClassification.objects.all().delete()
    print('数据清除完毕')


delete_all_faker_data()

# 创建Tag
tags = []
for _ in range(8):
    tag = models.Tag.objects.create(
        name=faker.unique.word(),
        is_show=True
    )
    tags.append(tag)

# 创建FirstClassification
first_classification = []
for _ in range(4):
    first_class = models.FirstClassification.objects.create(
        name=faker.word(),
        is_show=True
    )
    first_classification.append(first_class)

# 创建SecondClassification
second_classification = []
for first_class in first_classification:
    for _ in range(3):  # 每个一级分类下3个二级
        second_class = models.SecondClassification.objects.create(
            name=faker.word(),
            first_classification=first_class,
            is_show=True
        )
        second_classification.append(second_class)

# 创建 Note + NoteInfo + NoteList
for _ in range(20):
    title = faker.sentence(nb_words=3)
    content = faker.text(max_nb_chars=700)
    second_class = random.choice(second_classification)
    selected_tags = random.sample(tags, k=random.randint(1, 3))
    note_service.create_note_with_extra(
        title=title,
        content=content,
        second_classification=second_class,
        tags=selected_tags
    )

# 创建 Diary + DiaryInfo + DiaryList
for _ in range(20):
    title = faker.sentence(nb_words=3)
    content = faker.text(max_nb_chars=500)
    diary_service.create_diary_with_extra(
        title=title,
        content=content
    )

# 创建Essay + EssayInfo + EssayList
for _ in range(20):
    title = faker.sentence(nb_words=3)
    content = faker.text(max_nb_chars=700)
    selected_tags = random.sample(tags, k=random.randint(1, 3))
    essay_service.create_essay_with_extra(
        title=title,
        content=content,
        tags=selected_tags
    )

print('faker生产数据结束')