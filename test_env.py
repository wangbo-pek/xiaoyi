from dotenv import load_dotenv
import os

load_dotenv()

print("ALIYUN_OSS_ACCESS_KEY_ID =", os.getenv("ALIYUN_OSS_ACCESS_KEY_ID"))
print("ALIYUN_OSS_ACCESS_KEY_SECRET =", os.getenv("ALIYUN_OSS_ACCESS_KEY_SECRET"))
print("ALIYUN_OSS_BUCKET_NAME =", os.getenv("ALIYUN_OSS_BUCKET_NAME"))
print("ALIYUN_OSS_ENDPOINT =", os.getenv("ALIYUN_OSS_ENDPOINT"))