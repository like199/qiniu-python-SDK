# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json, base64


# 对文件进行base64编码
def base64_encode(data):
    data = base64.b64encode(data)
    if isinstance(data, bytes):
        data = data.decode('utf-8')
    return data


# 以二进制读取文件并进行base64编码
def encodestr(file):
    with open(file, 'rb') as f:
        data = f.read()
        ret = base64_encode(data)
    return ret


"""
人脸比对
文档：https://developer.qiniu.com/dora/api/6699/facecompare
"""

# 七牛账号的AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'

auth = QiniuMacAuth(access_key, secret_key)

# 请求URL
url = "http://face-compare.apistore.qiniu.com/facecompare"

# 对需要对比的图片A进行base64编码
IMAGEA_DATA1 = encodestr("图片A的本地路径")

# 对需要对比的图片B进行base64编码
IMAGEB_DATA2 = encodestr("图片B的本地路径")

# 请求体参数
body = {
    "imageA_b64": IMAGEA_DATA1,
    "imageB_b64": IMAGEB_DATA2,
    "image_type_B": 1,
    "rotate_A": True,
    "rotate_B": True
}

# 发起post请求
ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""人脸检测：https://developer.qiniu.com/dora/api/6817/facedetect"""

# 七牛账号的AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'
auth = QiniuMacAuth(access_key, secret_key)

# 请求URL
url = "http://face-detect.apistore.qiniu.com/facedetect"

# 对需要检测的图片进行base64编码
IMAGEA_DATA = encodestr("图片的本地路径")

# 请求体参数
body = {
    "image_b64": IMAGEA_DATA,
    "rotate": True
}

# 发起post请求
ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""
光线活体检测
文档：https://developer.qiniu.com/dora/api/6797/face-flashlive
"""

# 七牛账号的AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'

auth = QiniuMacAuth(access_key, secret_key)

# 请求URL
url = "http://face-flashlive.apistore.qiniu.com/flashlive"

# 对需要检测的视频进行base64编码
video_b64 = encodestr("视频文件的本地路径")

# 请求体参数
body = {
    "video_b64": video_b64
}

# 发起post请求
ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""
动作活体检测
文档：https://developer.qiniu.com/dora/api/6795/face-actlive
"""

# 七牛账号的AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'

auth = QiniuMacAuth(access_key, secret_key)

# 请求URL
url = "http://face-actlive.apistore.qiniu.com/actionlive"

# 对视频文件进行base64编码
video_b64 = encodestr("视频文件的本地路径")

# 请求体参数
body = {
    "video_b64": video_b64,
    "video_type": 1,
    "action_types": ["blink", "shake"]
}

# 发起post请求
ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""
防翻拍活体检测
文档：https://developer.qiniu.com/dora/api/6719/face-piclive
"""

# 七牛账号的AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'

auth = QiniuMacAuth(access_key, secret_key)

# 请求URL
url = "http://face-piclive.apistore.qiniu.com/picturelive"

# 对需要的检测图片进行base64编码
image_00 = encodestr("图片的本地路径")
image_01 = encodestr("图片的本地路径")

# 请求体参数
body = {
    "frames": [
        {
            "image_b64": image_00,
            "image_id": "image00",
            "quality": 80.0
        },
        {
            "image_b64": image_01,
            "image_id": "image01",
            "quality": 90.0
        },
    ]
}

# 发起post请求
ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))
