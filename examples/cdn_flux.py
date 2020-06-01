# -*- coding: utf-8 -*-
# flake8: noqa

"""
查询指定域名指定时间段内的流量
"""
import qiniu
from qiniu import CdnManager

# 账户ak，sk
access_key = ''
secret_key = ''

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

startDate = '2020-01-17'

endDate = '2020-01-17'

granularity = 'day'

urls = [
    "http://qiniu.bjhzkq.com/leida/1579164919679735SwLB6YZLLXF9YFtXu6gq3kU84CJ-O"
]

# 获得指定域名流量
ret, info = cdn_manager.get_flux_data(urls, startDate, endDate, granularity)

print(ret)
print(info)
