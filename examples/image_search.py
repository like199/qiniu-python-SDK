# -*- coding: utf-8 -*-
from qiniu import Auth, QiniuMacAuth, http
import requests, json

"""
以图搜图：https://developer.qiniu.com/dora/api/4680/image-search
"""

"""新建图像库：http://ai.qiniuapi.com/v1/image/group/<group_id>/new"""
# 图像库的唯一标识
group_id = ""

# 请求URL
url = 'http://ai.qiniuapi.com/v1/image/group/s%/new' % group_id

# AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'
auth = QiniuMacAuth(access_key, secret_key)

# 请求参数
body = {
    "data": [
        {
            "uri": "uri",  # 图片资源URL
            "attribute": {
                "id": "<自定义图片ID>",  # 自定义图片 id，在返回结果中显示，如果该字段为空，则会随机生成一个 id 并返回
                "label": "<图片标签>",  # 图片标签
                "desc": "<图片备注信息>"  # 内容可以是布尔值、数字、字符串、数组或 json，最大允许长度为4096字节
            }
        },
        {
            "uri": "<uri>",  # 图片资源URL
            "attribute": {
                "id": "<自定义图片ID>",
                "label": "<图片标签>",
                "desc": "<图片备注信息>"
            }
        }
    ]
}

ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""删除图像库：http://ai.qiniuapi.com/v1/image/group/<group_id>/remove"""
# 图像库的唯一标识
group_id = ""
# 请求URL
url = 'http://ai.qiniuapi.com/v1/image/group/s%/remove' % group_id

# AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'
auth = QiniuMacAuth(access_key, secret_key)

# 请求体参数
body = None

ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""添加图片：http://ai.qiniuapi.com/v1/image/group/<group_id>/add"""
# 图像库的唯一标识
group_id = ""

# 请求URL
url = 'http://ai.qiniuapi.com/v1/image/group/s%/add' % group_id

# AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'
auth = QiniuMacAuth(access_key, secret_key)

# 请求参数
body = {
    "data": [
        {
            "uri": "uri",  # 图片资源URL
            "attribute": {
                "id": "<自定义图片ID>",  # 自定义图片 id，在返回结果中显示，如果该字段为空，则会随机生成一个 id 并返回
                "label": "<图片标签>",  # 图片标签
                "desc": "<图片备注信息>"  # 内容可以是布尔值、数字、字符串、数组或 json，最大允许长度为4096字节
            }
        },
        {
            "uri": "<uri>",  # 图片资源URL
            "attribute": {
                "id": "<自定义图片ID>",
                "label": "<图片标签>",
                "desc": "<图片备注信息>"
            }
        }
    ]
}

ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""删除图片：http://ai.qiniuapi.com/v1/image/group/<group_id>/delete"""

# 图像库的唯一标识
group_id = ""

# 请求URL
url = 'http://ai.qiniuapi.com/v1/image/group/s%/delete' % group_id

# AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'
auth = QiniuMacAuth(access_key, secret_key)

# 请求参数
body = {
    "images": [
        "<image_id>",  # 图片唯一标识
        "<image_id>"
    ]
}

ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""显示所有图像库：http://ai.qiniuapi.com/v1/image/group"""
# 请求地址
url = 'http://ai.qiniuapi.com/v1/image/group'

# AK、SK
access_key = 'gd1VjcI1qYNcuRgrlutxnt7C0Z221MPOdYxhvPeA'
secret_key = 'uxYN_VYZvTqWcKq_sfHJfLk6yfBvMBapltbo5gVC'
auth = QiniuMacAuth(access_key, secret_key)

ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""显示指定图像库信息：http://ai.qiniuapi.com/v1/image/group/<group_id>/info"""

# 图像库ID
group_id = ""

# 请求地址：
url = "http://ai.qiniuapi.com/v1/image/group/%s/info" % group_id

# AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'

auth = QiniuMacAuth(access_key, secret_key)
ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""显示所有图片：http://ai.qiniuapi.com/v1/image/group/<group_id>?marker=<marker>&limit=<limit>"""

# AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'
auth = QiniuMacAuth(access_key, secret_key)

# 图像库ID
group_id = ""

# 上一次请求返回的标记，作为本次请求的起点信息，默认值为空字符串
marker = ""

# int类型；返回数量，范围为 1-1000，默认值为 1000
limit = 10

# 请求地址：
url = "http://ai.qiniuapi.com/v1/image/group/%s" % group_id + "?marker=" + marker + "&limit=" + limit

ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""显示指定图片信息：http://ai.qiniuapi.com/v1/image/group/<group_id>/image"""

# AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'
auth = QiniuMacAuth(access_key, secret_key)

# 图像库ID
group_id = ""

# 图片ID
id = ""

# 请求地址：
url = "http://ai.qiniuapi.com/v1/image/group/%s/image" % group_id

# 请求体
body = {
    "id": id
}

ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""图片搜索：http://ai.qiniuapi.com/v1/image/groups/search"""

# 请求URL
url = 'http://ai.qiniuapi.com/v1/image/groups/search'

# AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'
auth = QiniuMacAuth(access_key, secret_key)

# 请求参数
body = {
    "data": {
        "uri": "https://qiniu.oteeart.com/mmexport1577794762016.jpg"  # 搜索图片URL
    },
    "params": {
        "groups": [
            "works1"  # 图像库id
        ],
        "limit": 5,  # 匹配图片TOPN，默认为1，最大允许10000。若为-1，则返回所有匹配图片
        "threshold": 0.80  # 匹配图片的精度阈值，默认使用系统设置值。若该值小于系统设置值，则仍使用系统设置值
    }
}

ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))
