# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
from log import log_util
from config import config

config_info = config.get_config('cos')
secret_id = config_info['secret_id']
secret_key = config_info['secret_key']
region = config_info['region']
app_id = config_info['app_id']
bucket=config_info['bucket']
bucket_name = '%s-%s' %(bucket, app_id)
#print(secret_id,secret_key,region, bucket_name)
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
client = CosS3Client(config)
logger = log_util.get_log()



def list_objects(bucket_name, prefix=''):
    response = client.list_objects(
        Bucket=bucket_name,
        Prefix=prefix
    )
    return response

def upload_file_name(bucket_name, source_file, file_key):
    name_suffix = source_file.split('.')[1]
    if name_suffix == 'png':
        content_type = 'image/png'
    elif name_suffix =='jpg' or name_suffix =='jpeg':
        content_type = 'image/jpeg'
    elif name_suffix == 'webp':
        content_type = 'image/webp'
    elif name_suffix == 'gif':
        content_type = 'image/gif'
    else:
        content_type = ''
    with open(source_file, 'rb') as sf:
        response = client.put_object(
             Bucket=bucket_name,
             Body=sf,
             Key=file_key,
             ContentType=content_type
        )
    
def upload_default_bucket(source_file, file_key):
    upload_file_name(bucket_name, source_file, file_key)

def get_image_domain(bucket_name, region):
    return 'https://%s.cos.%s.myqcloud.com/' % (bucket_name, region)

def get_default_domain():
    return get_image_domain(bucket_name, region)

if __name__=="__main__":
    #list_objects(bucket_name)
    domain = get_default_domain()
    print(domain)
