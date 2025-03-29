from BackEnd import models


# 创建diary
def create_diary_with_extra(title, content):
    diary_obj = models.Diary.objects.create(
        title=title,
        markdown_content=content
    )

    models.DiaryList.objects.create(
        diary=diary_obj,
        title=title,
        brief=diary_obj.markdown_content[:85]
    )

    return diary_obj
