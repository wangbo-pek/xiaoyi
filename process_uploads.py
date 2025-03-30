import re
from pathlib import Path
from markdown import markdown

from BackEnd.utils.oss_upload import upload_file_to_oss
from BackEnd.services.note_import_service import create_note_and_list
from BackEnd import models

# 固定的markdown上传文件夹路径
UPLOAD_DIR_PATH = Path('/Users/wangbo/Documents/uploads')
# OSS路径前缀，不以 / 结尾
OSS_PREFIX = 'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/note_images'

print("当前扫描路径内容：", list(UPLOAD_DIR_PATH.glob("*")))

# 遍历所有mcpX文件
mcp_dirs_path = list(UPLOAD_DIR_PATH.glob('mcp*/'))

if not mcp_dirs_path:
    print('未找到任何mcp*文件')
    exit()

# 遍历所有的mcp文件夹
for mcp_dir_path in mcp_dirs_path:
    print('='*60)
    print(f'正在处理markdown文件：{mcp_dir_path.name}')

    # 获取.md的路径
    md_file_list = list(mcp_dir_path.glob('*.md'))
    if not md_file_list:
        print(f'未在{mcp_dir_path}中找到.md文件')
        continue
    md_file_path = md_file_list[0]
    print(f'找到markdown文件：{md_file_path.name}')

    # 获取封面cover路径
    cover_file_path = mcp_dir_path / 'cover.jpg'
    # 上传cover到OSS
    if cover_file_path.exists():
        oss_cover_key = f'note_covers/{mcp_dir_path.name}/cover.jpg'
        oss_cover_url = upload_file_to_oss(cover_file_path, oss_cover_key)
        print(f'找到封面图：{oss_cover_url}')
    else:
        oss_cover_url = None
        print('未找到封面图 cover.jpg')

    # 获取.md的内容
    with open(md_file_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # 获取.md内容中的pictures
    local_image_files_list = re.findall(r"!\[.*?]\((.*?)\)", markdown_content)

    # 构造本地pictures地址 --> OSS地址的映射
    image_mapping = {}
    for local_image_file in local_image_files_list:
        image_name = Path(local_image_file).name
        oss_image_url = f'{OSS_PREFIX}/{mcp_dir_path.name}/{image_name}'
        image_mapping[local_image_file] = oss_image_url

    # 替换.md中所有pictures地址为oss地址
    for local_image_file, oss_image_url in image_mapping.items():
        markdown_content = markdown_content.replace(f'{local_image_file}', f'{oss_image_url}')

    # 渲染HTML内容
    html_content = markdown(markdown_content, output_format='html')

    # 上传所有pictures到OSS
    for local_image_file in image_mapping.keys():
        image_name = Path(local_image_file).name
        local_image_path = mcp_dir_path / 'pic' / image_name
        oss_image_key = f'note_images/{mcp_dir_path.name}/{image_name}'
        upload_file_to_oss(local_image_path, oss_image_key)

    # 打印结果
    print(f'封面图OSS链接：{oss_cover_url if oss_cover_url else "无"}')
    print('markdown插图映射：')
    for k, v in image_mapping.items():
        print(f'{k} --> {v}')
    print('渲染后的HTML内容(前300字)：')
    print(html_content[:300])
    print('='*60)

    # 写入数据库
    default_second_classification = models.SecondClassification.objects.filter(id=401).first()
    default_tags = models.Tag.objects.filter(id__in=[281, 282])
    title = md_file_path.stem

    create_note_and_list(
        title=title,
        markdown_content=markdown_content,
        html_content=html_content,
        image_urls=list(image_mapping.values()),
        cover_img=oss_cover_url or '',
        second_classification=default_second_classification,
        tag_list=default_tags
    )
