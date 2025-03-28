from django.core.files.storage import Storage
from django.conf import settings
import oss2
from io import BytesIO


class AliyunOSSStorage(Storage):
    def __init__(self):
        self.auth = oss2.Auth(
            settings.ALIYUN_OSS_ACCESS_KEY_ID,
            settings.ALIYUN_OSS_ACCESS_KEY_SECRET
        )

        self.bucket = oss2.Bucket(
            self.auth,
            settings.ALIYUN_OSS_ENDPOINT,
            settings.ALIYUN_OSS_BUCKET_NAME
        )

        self.media_url = f"https://{settings.ALIYUN_OSS_BUCKET_NAME}.{settings.ALIYUN_OSS_ENDPOINT}/"

    def _save(self, name, content):
        # 把django的UploadFile转为二进制
        content.open()
        data = BytesIO(content.read())
        self.bucket.put_object(name, data)
        return name

    def exists(self, name):
        return self.bucket.object_exists(name)


    def url(self, name):
        return self.media_url + name
