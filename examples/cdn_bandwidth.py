# -*- coding: utf-8 -*-
from qiniu import Auth, QiniuMacAuth, CdnManager
from qiniu.services.cdn.manager import create_timestamp_anti_leech_url

"""批量查询动态加速之动态请求数：https://developer.qiniu.com/fusion/api/1230/traffic-bandwidth#5"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

# 起始日期，例如：2016-07-01
startDate = '2017-07-20'

# 结束日期，例如：2016-07-03
endDate = '2017-08-20'

# 粒度，取值：5min ／ hour ／day
granularity = 'day'

# 域名列表
domains = [
    'a.example.com',
    'b.example.com'
]

ret, info = cdn_manager.get_bandwidth_data(domains, startDate, endDate, granularity)

print(ret)
print(info)
