from faker import Faker
import random
from BackEnd import models
from BackEnd.services import note_service, essay_service, diary_service


print('faker开始生产数据')
# 实例化Faker，生产中文数据
faker = Faker('zh_CN')
from django import db
db.connections.close_all()

def fake_chinese_text(length=10):
    chars = '飞蛾局回复看来是蜂鸣器开哦文件哦我今日份哦快哦撇记得哦的一是不了在人有我了看法看得起我哦公开哦起哦恶趣味额请问恶化请我吃阀门打开几点回家甲方你请我额纪委莱卡棉物理课破读取带回去哦我就饿我饿他这中大来上个国以要就时出会可也你对生能而子那得于着下自之年过发后作里用道行所然家种事成方多经么去法学如都同现当没动面起看定天分还进好小部其些主样理心她本前开但因只从想实日军者无力它与长把机十民第公此已工使情明性知全三又关点正业外将两高间由问很最重并物手应战向头文体政美相见被利什二等产或新己制身果加西斯月话合回特代内信表化老给世位次度首单礼金大口径法兰快进到额外秋叶死哦记得私房钱文件偶尔全家都我考虑的呢我额飞机强迫第四三你啊额就放暑假看到你了咔哒我哦恶妇难舍难分我饿激发到哪杰克丹尼哦看的我请假明年到期我点进去破万李逵负荆破驱蚊扣颇尔哦去我怕诋毁门任常先海通哦啊带手机哦时间啊多可怕轻微哦哦裤衩子香菊胶囊起来我们哦就是的哦我请假软趴下教儿原东声提立及比员解水名真论处走义各入几口认条平系气她题活尔更别打权点风解'
    return ''.join(random.choices(chars, k=length))

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

# 创建Tag
tags = []
for _ in range(8):
    tag = models.Tag.objects.create(
        name=fake_chinese_text(length=random.randint(2, 5)),
        is_show=True
    )
    tags.append(tag)

# 创建FirstClassification
first_classification = []
for _ in range(4):
    first_class = models.FirstClassification.objects.create(
        name=fake_chinese_text(length=random.randint(4, 7)),
        is_show=True
    )
    first_classification.append(first_class)

# 创建SecondClassification
second_classification = []
for first_class in first_classification:
    for _ in range(3):  # 每个一级分类下3个二级
        second_class = models.SecondClassification.objects.create(
            name=fake_chinese_text(length=random.randint(2, 8)),
            first_classification=first_class,
            is_show=True
        )
        second_classification.append(second_class)

# 创建 Note + NoteList
for _ in range(20):
    title = fake_chinese_text(length=random.randint(5, 10))
    content = fake_chinese_text(length=random.randint(1200, 2000))
    second_class = random.choice(second_classification)
    selected_tags = random.sample(tags, k=random.randint(1, 3))
    note_service.create_note_with_extra(
        title=title,
        content=content,
        second_classification=second_class,
        tags=selected_tags
    )

# 创建 Diary + DiaryList
for _ in range(20):
    title = fake_chinese_text(length=random.randint(2, 8))
    content = fake_chinese_text(length=random.randint(500, 800))
    diary_service.create_diary_with_extra(
        title=title,
        content=content
    )

# 创建Essay + EssayList
for _ in range(20):
    title = fake_chinese_text(length=random.randint(5, 12))
    content = fake_chinese_text(length=random.randint(1500, 4000))
    selected_tags = random.sample(tags, k=random.randint(1, 3))
    essay_service.create_essay_with_extra(
        title=title,
        content=content,
        tags=selected_tags
    )

print('faker生产数据结束')
