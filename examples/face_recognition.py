# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json

"""
人脸检测
文档：https://developer.qiniu.com/dora/api/4281/face-detection
"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# 请求URL
url = "http://ai.qiniuapi.com/v1/face/detect"

# 请求参数
body = {
    "data": {
        # 图片资源地址（请求图片人脸部分面积不能小于60* 60)。
        "uri": "http://oayjpradp.bkt.clouddn.com/Audrey_Hepburn.jpg"
    }
}

ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""
1:1 人脸比对
文档：https://developer.qiniu.com/dora/api/4282/face-sim
"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# 请求URL
url = "http://ai.qiniuapi.com/v1/face/sim"

# 请求参数
body = {
    "data": [{
        # 图片资源地址（请求图片人脸部分面积不能小于60* 60)。
        "uri": "http://oayjpradp.bkt.clouddn.com/Audrey_Hepburn.jpg"
    },
        {"uri": "http://q7l1lwj1m.bkt.clouddn.com/Audrey_Hepburn.jpg"}
    ]
}

ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""
1:N 人脸比对
https://developer.qiniu.com/dora/api/4438/face-recognition
"""

"""1、新建人像库"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# 图像库的唯一标识
group_id = ""

# 请求URL
url = "http://ai.qiniuapi.com/v1/face/group/{0}/new".format(group_id)

# 请求参数
body = {
    "data": [
        {
            # 图片资源地址（请求图片人脸部分面积不能小于60* 60)。
            "uri": "http://oayjpradp.bkt.clouddn.com/Audrey_Hepburn.jpg",
            "attribute": {
                "id": "<id>",  # 自定义人脸 id，在返回结果中显示
                "name": "<name>",  # 人物姓名
                "mode": "<mode>",  # 人脸选择策略，可以设置为 SINGLE（只允许图片里面出现单张人脸，否则API返回错误） 或者 LARGEST（如果存在多张人脸，使用最大的人脸），默认SINGLE
                "desc": "<additional information>",  # 人脸图片的备注信息。内容可以是布尔值、数字、字符串、数组或 json，最大允许长度为4096字节
                "reject_bad_face": False
                # 是否拒绝低质量人脸入库，默认为不拒绝false。允许入库的人脸必须同时满足人脸质量为清晰clear以及方向为正脸up，人脸质量和人脸方向具体分类见表1 和表2
                # 注意： 当reject_bad_face为false时，返回人脸的质量信息，并且低质量人脸会正常入库
            }
        },
        {
            "uri": "http://q7l1lwj1m.bkt.clouddn.com/Audrey_Hepburn.jpg",
            "attribute": {
                "id": "<id>",
                "name": "<name>",
                "mode": "<mode>",
                "desc": "<additional information>",
                "reject_bad_face": False
            }
        }
    ]
}

ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""2、删除指定的人像库：如果人像库中含有人脸也一并删除。"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# 图像库的唯一标识
group_id = ""

# 请求URL
url = "http://ai.qiniuapi.com/v1/face/group/{0}/remove".format(group_id)

# 请求参数
body = None

ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""3、添加人脸：在指定人像库中添加人脸，返回新添加的人脸唯一标识。"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# 图像库的唯一标识
group_id = ""

# 请求URL
url = "http://ai.qiniuapi.com/v1/face/group/{0}/add".format(group_id)

# 请求参数
body = {
    "data": [
        {
            # 图片资源地址（请求图片人脸部分面积不能小于60* 60)。
            "uri": "http://oayjpradp.bkt.clouddn.com/Audrey_Hepburn.jpg",
            "attribute": {
                "id": "<id>",  # 自定义人脸 id，在返回结果中显示
                "name": "<name>",  # 人物姓名
                "mode": "<mode>",  # 人脸选择策略，可以设置为 SINGLE（只允许图片里面出现单张人脸，否则API返回错误） 或者 LARGEST（如果存在多张人脸，使用最大的人脸），默认SINGLE
                "desc": "<additional information>",  # 人脸图片的备注信息。内容可以是布尔值、数字、字符串、数组或 json，最大允许长度为4096字节
                "reject_bad_face": False
                # 是否拒绝低质量人脸入库，默认为不拒绝false。允许入库的人脸必须同时满足人脸质量为清晰clear以及方向为正脸up，人脸质量和人脸方向具体分类见表1 和表2
                # 注意： 当reject_bad_face为false时，返回人脸的质量信息，并且低质量人脸会正常入库
            }
        },
        {
            "uri": "http://q7l1lwj1m.bkt.clouddn.com/Audrey_Hepburn.jpg",
            "attribute": {
                "id": "<id>",
                "name": "<name>",
                "mode": "<mode>",
                "desc": "<additional information>",
                "reject_bad_face": False
            }
        }
    ]
}

ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""4、删除人脸：删除指定人像库中一个或多个人脸"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# 需要删除的人脸所在人像库的唯一标识
group_id = ""

# 请求URL
url = "http://ai.qiniuapi.com/v1/face/group/{0}/delete".format(group_id)

# 请求参数
body = {
    "faces": [
        "face_id",  # 需要删除的人脸 id
        "face_id"
    ]
}

ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""5、显示所有人像库：显示所有已建立的人像库的唯一id。"""

# 请求地址
url = "http://ai.qiniuapi.com/v1/face/group"

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""6、显示指定人像库信息：显示指定人像库中人脸个数。"""

# 人像库ID
group_id = ""

# 请求地址：
url = "http://ai.qiniuapi.com/v1/face/group/%s/info" % group_id

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"
auth = QiniuMacAuth(access_key, secret_key)

ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""7、显示所有人脸：显示指定的人像库中的所有人脸。"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"
auth = QiniuMacAuth(access_key, secret_key)

# 人像库ID
group_id = ""

# 上一次请求返回的标记，作为本次请求的起点信息，默认值为空字符串
marker = ""

# int类型；返回数量，范围为 1-1000，默认值为 1000
limit = 10

# 请求地址：
url = "http://ai.qiniuapi.com/v1/face/group/%s" % group_id + "?marker=" + marker + "&limit=" + limit

ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""显示指定人脸信息：显示某人像库指定一张人脸信息。"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# 人像库ID
group_id = ""

# 人脸ID
id = ""

# 请求地址：
url = "http://ai.qiniuapi.com/v1/face/group/%s/image" % group_id

# 请求体
body = {
    "id": id
}

ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""8、人脸库搜索：对于待搜索图片中检测到的每张人脸，在指定的人像库中返回其相似度最高的多张人脸 id。"""

# 请求URL
url = "http://ai.qiniuapi.com/v1/face/groups/search"

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# 请求参数
body = {
    "data": {
        "uri": "https://qiniu.oteeart.com/mmexport1577794762016.jpg"  # 搜索人脸URL
    },
    "params": {
        "groups": [
            "works1"  # 人像库id，最多只能在5个库里面搜索
        ],
        "limit": 5,  # 返回匹配度最高的前n个人脸，默认为1，最大允许10000。若为-1，则返回所有匹配人脸
        "threshold": 0.80,  # 匹配人脸的精度阈值，默认使用系统设置值（根据特征提取版本不同会有微小变动，目前取值0.4）。若该值小于系统设置值，则仍使用系统设置值
        "mode": "ALL",  # 人脸选择策略。可以设置为ALL（对图片中所有检测到的人脸进行搜索） 或者LARGEST（只对图片中最大的人脸进行搜索），默认ALL
        "use_quality": False
        # 搜索前是否使用人脸质量评估过滤人脸，默认为false。该值为true则不搜索待检测图片中的低质量人脸，false则对检测到的所有人脸进行搜索。
        # 低质量定义见上方表1 和 表2，该参数的优先级低于参数mode，即mode过滤后的人脸再使用该参数过滤。
    }
}

ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))
