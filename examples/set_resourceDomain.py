# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import QiniuMacAuth, BucketManager
import json

# 需要填写你的 Access Key 和 Secret Key
access_key = "<access_key>"
secret_key = "<secret_key>"

# 空间名
bucket_name = ""

# 镜像源的访问域名，必须设置为形如http(s)://source.com或http(s)://114.114.114.114的字符串
resourceDomain = "https://127.0.0.1"

# 回源时使用的Host头部值。参数值必须做URL 安全的 Base64 编码。可以填空字符串 "" 或不包含 /host/<EncodedHost> 部分，表示不额外指定 host
resourceHost = ""

q = QiniuMacAuth(access_key, secret_key)

bucket = BucketManager(q)

ret, res = bucket.set_bucketImagesource(bucket_name, resourceDomain, resourceHost)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))
