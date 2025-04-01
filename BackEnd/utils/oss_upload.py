import oss2
import os
from dotenv import load_dotenv
from pathlib import Path


# 加载.env文件中的oss配置信息
load_dotenv()
ACCESS_KEY_ID = os.getenv("ALIYUN_OSS_ACCESS_KEY_ID")
ACCESS_KEY_SECRET = os.getenv("ALIYUN_OSS_ACCESS_KEY_SECRET")
BUCKET_NAME = os.getenv("ALIYUN_OSS_BUCKET_NAME")
ENDPOINT = os.getenv("ALIYUN_OSS_ENDPOINT")

# 初始化oss认证和存储桶对象
auth = oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
bucket = oss2.Bucket(auth, ENDPOINT, BUCKET_NAME)


# 将本地文件上传到阿里oss
def upload_to_oss(local_path: Path, oss_key: str) -> str:
    """
    将本地文件上传到阿里oss
    :param local_path: 本地文件路径（Path对象）
    :param oss_key: OSS 中的文件路径（如 note_images/xxx/cover.jpg）
    :return: 上传后的完整 OSS URL
    """
    if not local_path.exists():
        print(f'本地文件不存在：{local_path}')
        return ''

    try:
        # 上传文件到oss
        with open(local_path, 'rb') as f:
            bucket.put_object(oss_key, f, headers={
                'Content-Disposition': 'inline',
                'Cache-Control': 'public, max-age=31536000'
            })
        # 拼接可访问的url (bucket+endpoint)
        url = f'https://{BUCKET_NAME}.{ENDPOINT}/{oss_key}'
        print(f'上传成功：{local_path.name} -> {url}')
        return url
    except Exception as e:
        print(f'上传失败：{local_path}，错误{e}')
        return ''
