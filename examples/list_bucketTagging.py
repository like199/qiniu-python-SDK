# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import QiniuMacAuth
from qiniu import BucketManager
import json

# 需要填写你的 Access Key 和 Secret Key
access_key = "<access_key>"
secret_key = "<secret_key>"

# 空间名
bucket_name = ""

q = QiniuMacAuth(access_key, secret_key)

bucket = BucketManager(q)

ret, res = bucket.list_bucketTagging(bucket_name)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))
