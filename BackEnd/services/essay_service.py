from BackEnd import models


# 创建essay
def create_essay_with_extra(title, content, tags):
    essay_obj = models.Essay.objects.create(
        title=title,
        markdown_content=content
    )

    essay_list_obj = models.EssayList.objects.create(
        essay=essay_obj,
        title=title,
        subtitle=essay_obj.markdown_content[:15],
        brief=essay_obj.markdown_content[:85]
    )
    essay_list_obj.tags.set(tags)

    return essay_obj