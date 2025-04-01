from BackEnd.models import Note, NoteList, Diary, DiaryList, Tag, FirstClassification, SecondClassification


def create_note_and_list(title, subtitle, brief, image_urls, content, cover_url, first_classification,
                         second_classification, tags):
    # 获取二级分类
    try:
        first_obj = FirstClassification.objects.get(name=first_classification)
        second_obj = SecondClassification.objects.get(
            name=second_classification,
            first_classification=first_obj
        )
    except FirstClassification.DoesNotExist:
        print(f'一级分类不存在：{first_classification}')
        return
    except SecondClassification.DoesNotExist:
        print(f'二级分类不存在：{second_classification}')
        return

    # 创建Note
    note = Note.objects.create(
        title=title,
        markdown_content=content,
        image_urls=image_urls
    )

    # 创建NoteList
    note_list = NoteList.objects.create(
        title=title,
        subtitle=subtitle,
        brief=brief,
        cover_img=cover_url,
        note=note,
        second_classification=second_obj
    )

    # 添加标签
    for tag_name in tags:
        tag, _ = Tag.objects.get_or_create(name=tag_name)
        note_list.tags.add(tag)


def create_diary_and_list(title, brief, image_urls, content, cover_url):
    diary = Diary.objects.create(
        title=title,
        markdown_content=content,
        image_urls=image_urls
    )

    DiaryList.objects.create(
        title=title,
        brief=brief,
        cover_img=cover_url,
        diary=diary
    )
