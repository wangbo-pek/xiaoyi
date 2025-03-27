from BackEnd import models


# 创建diary
def create_diary_with_extra(title, content):
    diary_obj = models.Diary.objects.create(
        title=title,
        content=content
    )

    models.DiaryList.objects.create(
        diary=diary_obj,
        cover_img='https://channel-jk.com/wp-content/uploads/2021/08/2598173953459235257.jpg',
        title=title,
        subtitle=diary_obj.content[:15],
        brief=diary_obj.content[:64]
    )

    return diary_obj
