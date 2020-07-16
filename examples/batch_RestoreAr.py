# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http, urlsafe_base64_encode
import json


# 格式化解冻数据
def batch_data(filename, freezeAfterDays):
    data = ""
    for i in filename:
        entry = f"{bucket_name}:{i}"
        encodedEntryURI = urlsafe_base64_encode(entry)
        data = data + f"op=/restoreAr/{encodedEntryURI}/freezeAfterDays/{freezeAfterDays}&"
    return data[0:-1]


# 七牛账号的AK、SK
access_key = '公钥'
secret_key = '私钥'

auth = QiniuMacAuth(access_key, secret_key)

# 解冻文件存储空间名
bucket_name = ""

# 解冻有效时长
freezeAfterDays = 2

# 需要解冻的文件名（文件名需要在同一空间）
filename = ["15758584210000141.png", "1575858514000877.jpeg", "159187349972000&1.m4a"]

# 批量解冻请求地址
restoreArurl = 'http://rs.qbox.me/batch?'
url = restoreArurl + batch_data(filename, freezeAfterDays)

body = {}

# 发起POST请求
ret, res = http._post_with_qiniu_mac(url, body, auth)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))
