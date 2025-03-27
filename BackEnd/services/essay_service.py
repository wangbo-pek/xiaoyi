from BackEnd import models


# 创建essay
def create_essay_with_extra(title, content, tags):
    essay_obj = models.Essay.objects.create(
        title=title,
        content=content
    )

    essay_list_obj = models.EssayList.objects.create(
        essay=essay_obj,
        cover_img='https://channel-jk.com/wp-content/uploads/2021/08/2598173953459235257.jpg',
        title=title,
        subtitle=essay_obj.content[:15],
        brief=essay_obj.content[:64]
    )
    essay_list_obj.tags.set(tags)

    return essay_obj