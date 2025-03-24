from faker import Faker
import random
from BackEnd.models import (Note, NoteInfo, Diary, Essay, EssayInfo, Tag, FirstClassification, SecondClassification)

# 实例化Faker，生产中文数据
faker = Faker('zh_CN')


# 清除旧数据(optional)
def delete_all_faker_data():
    Note.objects.all().delete()
    NoteInfo.objects.all().delete()
    Diary.objects.all().delete()
    EssayInfo.objects.all().delete()
    Tag.objects.all().delete()
    FirstClassification.objects.all().delete()
    SecondClassification.objects.all().delete()


delete_all_faker_data()

# 创建Tag
tags = []
for _ in range(5):
    tag = Tag.objects.create(
        name=faker.word(),
        is_show=True
    )
    tags.append(tag)

# 创建FirstClassification
first_classification = []
for _ in range(3):
    first_class = FirstClassification.objects.create(
        name=faker.word(),
        is_show=True
    )
    first_classification.append(first_class)

# 创建SecondClassification
second_classification = []
for first_class in first_classification:
    for _ in range(2):  # 每个一级分类下2个二级
        sc = SecondClassification.objects.create(
            name=faker.word(),
            first_classification=first_class,
            is_show=True
        )
        second_classification.append(sc)

# 创建 Note + NoteInfo
for _ in range(10):
    note = Note.objects.create(
        title=faker.sentence(nb_words=3),
        brief=faker.text(max_nb_chars=60),
        content=faker.text(max_nb_chars=500),
        is_show=True,
        second_classification=random.choice(second_classification),
    )
    note.tags.set(random.sample(tags, k=random.randint(1, 3)))
    # NoteInfo.objects.create(note=note)

# 创建 Essay + EssayInfo
for _ in range(8):
    essay = Essay.objects.create(
        title=faker.sentence(nb_words=4),
        brief=faker.text(max_nb_chars=60),
        content=faker.text(max_nb_chars=600),
        is_show=True,
        is_reprint=random.choice([True, False]),
        reprint_from=faker.company() if random.choice([True, False]) else '',
        reprint_whom=faker.name() if random.choice([True, False]) else '',
    )
    essay.tags.set(random.sample(tags, k=random.randint(1, 3)))
    # EssayInfo.objects.create(essay=essay)
