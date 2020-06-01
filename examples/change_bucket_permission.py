# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth
from qiniu import BucketManager

# 需要填写你的 Access_Key 和 Secret_Key
access_key = '<access_key>'
secret_key = '<secret_key>'

# 空间名
bucket_name = ""
# private 参数必须是str类型，0表示公有空间，1表示私有空间
private = "0"
q = Auth(access_key, secret_key)

bucket = BucketManager(q)

ret, info = bucket.change_bucket_permission(bucket_name, private)
print(info)
