# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth
from qiniu import BucketManager

"""获取空间绑定的加速域名"""

# 需要填写你的 Access_Key 和 Secret_Key
access_key = '<access_key>'
secret_key = '<secret_key>'

# 空间名
bucket_name = ''

q = Auth(access_key, secret_key)

bucket = BucketManager(q)

ret, info = bucket.bucket_domain(bucket_name)
print(info)
