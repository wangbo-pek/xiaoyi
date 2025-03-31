from BackEnd import models
import re


# 从markdown中，跳过所有markdown语法，来获取文字作为subtitle、brief
def extract_text(md_text: str, max_length: int = 30) -> str:
    # 去掉图片语法
    cleaned = re.sub(r"!\[.*?]\(.*?\)", "", md_text)
    # 去掉标题语法 (比如 #, ##, ### 等)
    cleaned = re.sub(r"^#{1,6}\s*", "", cleaned, flags=re.MULTILINE)
    # 去掉粗体语法 (**bold**)
    cleaned = re.sub(r"\*\*.*?\*\*", "", cleaned)
    # 去掉斜体语法 (*italic* 或 _italic_)
    cleaned = re.sub(r"\*.*?\*|_.*?_", "", cleaned)
    # 去掉链接语法 ([text](url))
    cleaned = re.sub(r"\[.*?]\(.*?\)", "", cleaned)
    # 去掉下划线语法 (_underlined_)
    cleaned = re.sub(r"(_.*?_)","", cleaned)
    # 去掉删除线语法 (~~strikethrough~~)
    cleaned = re.sub(r"~~.*?~~", "", cleaned)
    # 去掉引用语法 (> 引用内容)
    cleaned = re.sub(r"^>\s*", "", cleaned, flags=re.MULTILINE)
    # 去掉代码块语法 (包括行内代码 `code` 和块级代码 ```code```)
    cleaned = re.sub(r"`.*?`", "", cleaned)  # 去掉行内代码
    cleaned = re.sub(r"```[\s\S]*?```", "", cleaned)  # 去掉块级代码
    # 去掉有序列表 (1. item)
    cleaned = re.sub(r"^\d+\.\s*", "", cleaned, flags=re.MULTILINE)
    # 去掉无序列表 (- item, * item)
    cleaned = re.sub(r"^[-*+]\s*", "", cleaned, flags=re.MULTILINE)
    # 去掉多余的空白字符
    cleaned = cleaned.strip()

    # 返回前 max_length 个字符作为 brief 或 subtitle
    return cleaned[:max_length]


def create_note_and_list(title, markdown_content, image_urls, cover_img, second_classification, tag_list):
    # 创建Note实例
    note_obj = models.Note.objects.create(
        title=title,
        markdown_content=markdown_content,
        table_of_content='',
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
