# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import QiniuMacAuth, http
from qiniu import BucketManager
import json

# 需要填写你的 Access Key 和 Secret Key
access_key = "<access_key>"
secret_key = "<secret_key>"

# 空间名
bucket_name = ""

body = {
    "Tags": [
        {
            # key: 标签名称，最大64Byte，不能为空且大小写敏感，不能以kodo为前缀(预留), 不支持中文字符，可使用的字符有：字母，数字，空格，+ - = . _ : / @
            "Key": "",
            # value：标签值，最大128Byte，不能为空且大小写敏感，不支持中文字符，可使用的字符有：字母，数字，空格，+ - = . _ : / @
            "Value": ""
        }
    ]
}

q = QiniuMacAuth(access_key, secret_key)

bucket = BucketManager(q)

ret, res = bucket.set_bucketTagging(bucket_name, body)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))
