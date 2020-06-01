# -*- coding: utf-8 -*-
# flake8: noqa

"""
查询指定域名指定时间段内的带宽
"""
import qiniu
from qiniu import CdnManager

# 账户ak，sk
access_key = ''
secret_key = ''

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

# 起始日期，例如：2016-07-01
startDate = '2017-07-20'

# 结束日期，例如：2016-07-03
endDate = '2017-08-20'

# 粒度，取值：5min ／ hour ／day
granularity = 'day'

# 域名列表
urls = [
    'a.example.com',
    'b.example.com'
]

ret, info = cdn_manager.get_dynreqcount_data(urls, startDate, endDate, granularity)

print(ret)
print(info)
