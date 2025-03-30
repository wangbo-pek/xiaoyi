from BackEnd import models
import re


# 从markdown中，跳过图片语法![]()，来获取文字作为subtitle、brief
def extract_text(md_text: str, max_length: int = 30) -> str:
    cleaned = re.sub(r"!\[.*?]\(.*?\)", "", md_text)
    cleaned = cleaned.strip()
    return cleaned[:max_length]


def create_note_and_list(title, markdown_content, html_content, image_urls, cover_img, second_classification, tag_list):
    # 创建Note实例
    note_obj = models.Note.objects.create(
        title=title,
        markdown_content=markdown_content,
        html_content=html_content,
        image_urls=image_urls
    )

    # 创建NoteList实例
    note_list_obj = models.NoteList.objects.create(
        title=title,
        subtitle=extract_text(markdown_content, 20),
        brief=extract_text(markdown_content, 80) + '... ...',
        cover_img=cover_img,
        note=note_obj,
        second_classification=second_classification
    )

    note_list_obj.tags.set(tag_list)
    return note_obj
