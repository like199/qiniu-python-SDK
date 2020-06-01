# -*- coding: utf-8 -*-
# flake8: noqa

"""
获取指定域名指定时间内的日志链接
"""
import qiniu
from qiniu import CdnManager

# 账户ak，sk
access_key = 'TrSdUa-nlpbCH0NA9eQ1CSUzd_-4V8dRu41l--HD'
secret_key = 'M_evLMsIt5MkcSMOS7SUQXLV_NrdzmFuuLcKFfru'

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

log_date = '2020-02-05'

urls = [
    'pcppc4i3f.bkt.clouddn.com'
]

ret, info = cdn_manager.get_log_list_data(urls, log_date)

print(ret)
print(info)
