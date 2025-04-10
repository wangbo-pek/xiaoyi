import json
import re
from pathlib import Path

from BackEnd.utils.oss_upload import upload_to_oss
from BackEnd.utils.db_create import create_note_and_list, create_diary_and_list


# 用于提取markdown中的纯文本摘要
def extract_text(md_text: str, max_length: int = 100) -> str:
    cleaned = re.sub(r"!\[.*?]\(.*?\)", "", md_text)
    cleaned = re.sub(r"^#{1,6}\s*", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"\*\*.*?\*\*", "", cleaned)
    cleaned = re.sub(r"\*.*?\*|_.*?_", "", cleaned)
    cleaned = re.sub(r"\[.*?]\(.*?\)", "", cleaned)
    cleaned = re.sub(r"(_.*?_)", "", cleaned)
    cleaned = re.sub(r"~~.*?~~", "", cleaned)
    cleaned = re.sub(r"^>\s*", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"`.*?`", "", cleaned)
    cleaned = re.sub(r"```[\s\S]*?```", "", cleaned)
    cleaned = re.sub(r"^\d+\.\s*", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"^[-*+]\s*", "", cleaned, flags=re.MULTILINE)
    cleaned = cleaned.strip()
    return cleaned[:max_length]


def process_uploads():

    print('1')
    upload_path = Path("/Users/wangbo/Documents/uploads")
    if not upload_path.exists():
        print(f"错误：上传目录不存在：{upload_path}")
        return

    for folder in upload_path.iterdir():
        folder_name = folder.name.strip()
        if not folder.is_dir() or folder_name.endswith('_uploaded') or folder_name.endswith('_preparation'):
            continue

        print(f'\n\u2728 开始处理：{folder_name}')

        is_note = folder_name.startswith('note')
        is_diary = folder_name.startswith('diary')
        if not is_note and not is_diary:
            print(f'跳过{folder_name}，不是note或diary')

        # 获取路径
        md_file = None
        for f in folder.iterdir():
            if f.suffix == '.md':
                md_file = f
                break

        cover_path = folder / 'cover.jpg'
        pictures_path = folder / 'pictures'

        if not md_file or not cover_path.exists():
            print(f'缺少必要文件，跳过{folder_name}')
            continue

        # 上传封面图
        cover_url = upload_to_oss(cover_path, f'images/{folder_name}/cover.jpg')

        # 上传插图并建立映射
        image_mapping = {}
        if pictures_path.exists():
            for image_file in pictures_path.iterdir():
                if image_file.suffix.lower() not in {'.jpg', '.jpeg', '.png', '.gif', '.webp'}:
                    continue
                oss_key = f'images/{folder_name}/pictures/{image_file.name}'
                oss_url = upload_to_oss(image_file, oss_key)
                image_mapping[image_file.name] = oss_url
        image_urls = list(image_mapping.values())

        # 读取markdown内容并替换插图路径为oss_url
        with md_file.open('r', encoding='utf-8') as f:
            md_content = f.read()

        for image_name, oss_url in image_mapping.items():
            md_content = md_content.replace(f'pictures/{image_name}', oss_url)

        title = md_file.stem
        lines = md_content.strip().splitlines()

        if is_note:
            # 提取最后一行分类/标签
            category = ''
            tags = []
            if lines:
                last_line = lines[-1]
                if last_line.startswith('@'):
                    parts = last_line.split()
                    if parts:
                        category = parts[0][1:].strip()
                        for part in parts[1:]:
                            if part.startswith('#'):
                                tags.append(part[1:])
                    # 删除分类标签行
                    lines = lines[:-1]
                    md_content = '\n'.join(lines)

            # 提取引用作为 brief
            brief_quote = ''
            for line in lines:
                if line.strip().startswith('>'):
                    brief_quote = line
                    break
            brief = extract_text(brief_quote)

            create_note_and_list(
                title=title,
                brief=brief,
                content=md_content,
                cover_url=cover_url,
                image_urls=image_urls,
                category=category,
                tags=tags
            )

        elif is_diary:
            # 提取第一行 brief
            brief = ''
            if lines:
                first_line = lines[0]
                if first_line.startswith('@'):
                    brief = first_line[1:].strip()
                    lines = lines[1:]
                    md_content = '\n'.join(lines)
                else:
                    brief = extract_text(md_content)

            create_diary_and_list(
                title=title,
                brief=brief,
                content=md_content,
                cover_url=cover_url,
                image_urls=image_urls
            )

        # 重命名文件夹
        new_folder = folder.with_name(folder_name + '_uploaded')
        folder.rename(new_folder)
        print(f'\u2705 处理完毕并已重新命名：{new_folder.name}')


if __name__ == '__main__':
    process_uploads()
