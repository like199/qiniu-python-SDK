# -*- coding: utf-8 -*-
import json, hmac, base64
from hashlib import sha1


def qiniu_token(access_key, secret_key, method, path, host, contentType="application/x-www-form-urlencoded",
                query=None, body=None):
    """
    无七牛特殊请求头参数的鉴权token
    """
    if query:
        # 签算的原始字符串
        signingStr = method + " " + path + "?" + query + "\nHost: " + host + "\n\n" + json.dumps(body)
    elif contentType == "application/x-www-form-urlencoded":
        # 签算的原始字符串
        signingStr = method + " " + path + "\nHost: " + host + "\nContent-Type: " + contentType + "\n\n"
    else:
        # 签算的原始字符串
        signingStr = method + " " + path + "\nHost: " + host + "\nContent-Type: " + contentType + "\n\n" + json.dumps(
            body)

    token = (
        base64.urlsafe_b64encode(
            (hmac.new(secret_key.encode("utf-8"), signingStr.encode("utf-8"), sha1)).digest())).decode(
        "utf-8")

    qiniuToken = "Qiniu " + f"{access_key}:{token}"
    return qiniuToken


def qiniu_headers(headers):
    """
    格式化 七牛特殊请求头
    :param headers:请求头参数，列表格式
    :return:
    """
    res = ""
    for key in headers:
        if key.startswith("X-Qiniu-"):
            res += key + ": %s\n" % (headers.get(key))
    return res


def qiniu_request_token(access_key, secret_key, method, path, host, headers,
                        contentType="application/x-www-form-urlencoded",
                        query=None, body=None):
    """
    带请求头参数的鉴权token
    """
    headers = qiniu_headers(headers)
    if query:
        # 签算的原始字符串
        signingStr = method + " " + path + "?" + query + "\nHost: " + host + "\n" + headers + "\n\n" + json.dumps(body)
    elif contentType == "application/x-www-form-urlencoded":
        # 签算的原始字符串
        signingStr = method + " " + path + "\nHost: " + host + "\nContent-Type: " + contentType + "\n\n" + "\n" + headers
    else:
        # 签算的原始字符串
        signingStr = method + " " + path + "\nHost: " + host + "\nContent-Type: " + contentType + "\n" + headers + "\n\n" + json.dumps(
            body)

    token = (
        base64.urlsafe_b64encode(
            (hmac.new(secret_key.encode("utf-8"), signingStr.encode("utf-8"), sha1)).digest())).decode(
        "utf-8")

    qiniuToken = "Qiniu " + f"{access_key}:{token}"
    return qiniuToken


if __name__ == '__main__':
    # AK、SK
    access_key = "私钥"
    secret_key = "公钥"

    # 请求方式
    method = "POST"

    # 请求路径
    path = "/sisyphus/fetch"

    # 请求参数
    query = ""

    # 请求HOST
    host = "api-z0.qiniu.com"

    # content-type类型
    contentType = "application/json"

    # 请求头
    qheaders = ""

    # 请求体:如果您设置了请求Body，并且设置Content-Type不为"application/octet-stream"类型，Body也需要加入待签名字符串
    body = {
        "url": "",
        "bucket": ""
    }

    qiniuToken = qiniu_token(access_key, secret_key, method, path, host, contentType, body=body)

    print(qiniuToken)
