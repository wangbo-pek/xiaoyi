from BackEnd.models import Note, NoteList, Diary, DiaryList, Tag, Category


def create_note_and_list(title, brief, image_urls, content, cover_url, category, tags):
    print('create_note_and_list >>>>>> begin')
    # 获取分类
    try:
        category_obj = Category.objects.get(name=category,)
    except Category.DoesNotExist:
        print(f'分类不存在：{category}')
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
        brief=brief,
        cover_img=cover_url,
        note=note,
        category=category_obj
    )

    # 添加标签
    for tag_name in tags:
        tag, _ = Tag.objects.get_or_create(name=tag_name)
        note_list.tags.add(tag)


def create_diary_and_list(title, brief, image_urls, content, cover_url):
    print('create_diary_and_list >>>>>> begin')
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
