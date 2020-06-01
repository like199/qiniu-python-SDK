# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json

"""
数据统计接口
https://developer.qiniu.com/kodo/api/3906/statistic-interface
"""

"""1、标准存储当前存储量统计：https://developer.qiniu.com/kodo/api/3908/statistic-space"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# 存储空间名称，是一个条件请求参数
bucket = "upload25"

# 必填，起始日期字符串，闭区间，例如： 20060102150405
begin = "20200301"

# 必填，结束日期字符串，开区间，例如： 20060102150405
end = "20200323"

# 必填，时间粒度，支持 day；当天支持5min、hour、day
g = "hour"

# 存储区域：z0 华东；z1 华北；z2 华南；na0 北美；as0 东南亚；是条件请求参数
region = "z0"

# 值为size，表示流量 (Byte)
select = "size"

# 请求地址：
url = "http://api.qiniu.com/v6/space?begin={0}&end={1}&g={2}".format(begin, end, g)

ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""2、标准存储当前文件量统计：https://developer.qiniu.com/kodo/api/3914/count"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# 存储空间名称，是一个条件请求参数
bucket = "upload25"

# 必填，起始日期字符串，闭区间，例如： 20060102150405
begin = "20200301"

# 必填，结束日期字符串，开区间，例如： 20060102150405
end = "20200323"

# 必填，时间粒度，支持 day；当天支持5min、hour、day
g = "hour"

# 存储区域：z0 华东；z1 华北；z2 华南；na0 北美；as0 东南亚；是条件请求参数
region = "z0"

# 值为size，表示流量 (Byte)
select = "size"

# 请求地址：
url = "http://api.qiniu.com/v6/count?begin={0}&end={1}&g={2}".format(begin, end, g)

ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""3、低频存储当前存储量统计：https://developer.qiniu.com/kodo/api/3910/space-line"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# 存储空间名称，是一个条件请求参数
bucket = "upload25"

# 必填，起始日期字符串，闭区间，例如： 20060102150405
begin = "20200301"

# 必填，结束日期字符串，开区间，例如： 20060102150405
end = "20200323"

# 必填，时间粒度，支持 day；当天支持5min、hour、day
g = "hour"

# 存储区域：z0 华东；z1 华北；z2 华南；na0 北美；as0 东南亚；是条件请求参数
region = "z0"

# 值为size，表示流量 (Byte)
select = "size"

# 请求地址：
url = "http://api.qiniu.com/v6/space_line?begin={0}&end={1}&g={2}".format(begin, end, g)

ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""4、低频存储当前文件量统计：https://developer.qiniu.com/kodo/api/3915/count-line"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# 存储空间名称，是一个条件请求参数
bucket = "upload25"

# 必填，起始日期字符串，闭区间，例如： 20060102150405
begin = "20200301"

# 必填，结束日期字符串，开区间，例如： 20060102150405
end = "20200323"

# 必填，时间粒度，支持 day；当天支持5min、hour、day
g = "hour"

# 存储区域：z0 华东；z1 华北；z2 华南；na0 北美；as0 东南亚；是条件请求参数
region = "z0"

# 值为size，表示流量 (Byte)
select = "size"

# 请求地址：
url = "http://api.qiniu.com/v6/count_line?begin={0}&end={1}&g={2}".format(begin, end, g)

ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""5、归档存储当前存储量统计：https://developer.qiniu.com/kodo/api/6462/space-archive"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# 存储空间名称，是一个条件请求参数
bucket = "upload25"

# 必填，起始日期字符串，闭区间，例如： 20060102150405
begin = "20200301"

# 必填，结束日期字符串，开区间，例如： 20060102150405
end = "20200323"

# 必填，时间粒度，支持 day；当天支持5min、hour、day
g = "hour"

# 存储区域：z0 华东；z1 华北；z2 华南；na0 北美；as0 东南亚；是条件请求参数
region = "z0"

# 值为size，表示流量 (Byte)
select = "size"

# 请求地址：
url = "http://api.qiniu.com/v6/space_archive?begin={0}&end={1}&g={2}".format(begin, end, g)

ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""6、归档存储当前文件量统计：https://developer.qiniu.com/kodo/api/6463/count-archive"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# 存储空间名称，是一个条件请求参数
bucket = "upload25"

# 必填，起始日期字符串，闭区间，例如： 20060102150405
begin = "20200301"

# 必填，结束日期字符串，开区间，例如： 20060102150405
end = "20200323"

# 必填，时间粒度，支持 day；当天支持5min、hour、day
g = "hour"

# 存储区域：z0 华东；z1 华北；z2 华南；na0 北美；as0 东南亚；是条件请求参数
region = "z0"

# 值为size，表示流量 (Byte)
select = "size"

# 请求地址：
url = "http://api.qiniu.com/v6/count_archive?begin={0}&end={1}&g={2}".format(begin, end, g)

ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""7、获取跨区域同步流量统计：https://developer.qiniu.com/kodo/api/3911/blob-transfer"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# 必填，起始日期字符串，闭区间，例如： 20060102150405
begin = "20200301"

# 必填，结束日期字符串，开区间，例如： 20060102150405
end = "20200323"

# 必填，时间粒度，支持 5min hour day month
g = "day"

# 必填，值为size，表示流量 (Byte)
select = "size"

# $is_oversea，是否为海外同步；0 国内，1 海外
is_oversea = ""

# $taskid，任务ID
taskid = ""

# 请求地址：
url = "http://api.qiniu.com/v6/blob_transfer?begin={0}&end={1}&g={2}&select={3}".format(begin, end, g, select)

ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""8、获取存储类型请求次数统计：https://developer.qiniu.com/kodo/api/3913/rs-chtype"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# $bucket，存储空间名称，是一个条件请求参数
bucket = "upload25"

# region，必填，起始日期字符串，闭区间，例如： 20060102150405
begin = "20200301"

# 必填，结束日期字符串，开区间，例如： 20060102150405
end = "20200323"

# 必填，时间粒度，支持 5min hour day month
g = "day"

# $region，存储区域：z0 华东；z1 华北；z2 华南；na0 北美；as0 东南亚；是条件请求参数
region = "z0"

# 必填，值为hits，表示请求数
select = "hits"

# 请求地址：
url = "http://api.qiniu.com/v6/rs_chtype?begin={0}&end={1}&g={2}&select={3}".format(begin, end, g, select)

ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""9、获取外网流出流量统计，CDN回源流出流量统计，数据读取统计， GET请求次数统计：https://developer.qiniu.com/kodo/api/3820/blob-io"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# $bucket，存储空间名称，是一个条件请求参数
bucket = "upload25"

# $domain，空间访问域名
domain = ""

# 必填，起始日期字符串，闭区间，例如： 20060102150405
begin = "20200301"

# 必填，结束日期字符串，开区间，例如： 20060102150405
end = "20200323"

# 必填，时间粒度，支持 5min hour day month
g = "hour"

# $ftype，存储类型；0 标准存储，1 低频存储，2 归档存储
ftype = "0"

# $region，存储区域：z0 华东；z1 华北；z2 华南；na0 北美；as0 东南亚；是条件请求参数
region = "z0"

"""
查询外网下载流量：select=flow&$src-C程序=origin
查询CDN回源流量：select=flow&$src-C程序=!origin&$src-C程序=!atlab&$src-C程序=!inner&$src-C程序=!ex
查询下载请求次数：select=hits&$src-C程序=origin&$src-C程序=inner
"""
# 必填，值字段；flow 流量（Byte），hits GET 请求次数
select = "flow"

# 请求来源；origin 用户直接到源站的请求，inner 专线或内网请求
src = ""

# 请求地址：
url = "http://api.qiniu.com/v6/blob_io?begin={0}&end={1}&g={2}&select={3}".format(begin, end, g, select)

ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""10、获取 PUT 请求次数统计：https://developer.qiniu.com/kodo/api/3912/rs-put"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

# $bucket,存储空间名称，是一个条件请求参数
bucket = "upload25"

# 必填，起始日期字符串，闭区间，例如： 20060102150405
begin = "20200301"

# 必填，结束日期字符串，开区间，例如： 20060102150405
end = "20200323"

# 必填，时间粒度，支持 5min hour day month
g = "day"

# $region，存储区域：z0 华东；z1 华北；z2 华南；na0 北美；as0 东南亚；是条件请求参数
region = "z0"

# 必填，值为hits，表示请求数
select = "hits"

# $ftype，存储类型；0 标准存储，1 低频存储，2 归档存储
ftype = "0"

# 请求地址：
url = "http://api.qiniu.com/v6/rs_put?begin={0}&end={1}&g={2}&select={3}".format(begin, end, g, select)

ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))
