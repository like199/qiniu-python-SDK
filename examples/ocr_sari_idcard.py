# -*- coding: utf-8 -*-
from qiniu import Auth, QiniuMacAuth, http
import requests, json

"""
旧版OCR身份证识别（idcard）
https://developer.qiniu.com/dora/api/4276/ocr-sari-idcard
"""

# AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'

auth = QiniuMacAuth(access_key, secret_key)

# 请求URL
url = 'http://ai.qiniuapi.com/v1/ocr/idcard'

# 请求参数
body = {
    "data": {
        # 身份证图片链接
        "uri": ""
    }
}

ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

