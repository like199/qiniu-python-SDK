# -*- coding: utf-8 -*-
# flake8: noqa
import qiniu
from qiniu import CdnManager

"""
日志分析
https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis
"""

"""1、区域运营商流量查询：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#4"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

# 域名列表，总数不超过100条
domains = [
    'pcppc4i3f.bkt.clouddn.com'
]

# 粒度，可选项为 5min、1hour、1day
freq = '1day'

# 区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
regions = [
    ""
]

# ISP运营商，比如all(所有 ISP)，telecom(电信)，unicom(联通)，mobile(中国移动)，drpeng(鹏博士)，tietong(铁通)，cernet(教育网)
isp = ""

# 开始时间，格式为：2006-01-02。起止最大间隔为31天
startDate = ""

# 结束时间，格式为：2006-01-02。起止最大间隔为31天
endDate = ""

ret, info = cdn_manager.get_loganalyze_traffic(domains, freq, regions, isp, startDate, endDate)

print(ret)
print(info)

"""2、区域运营商带宽查询：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#5"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

# 域名列表，总数不超过100条
domains = [
    'q7l1lwj1m.bkt.clouddn.com'
]

# 粒度，可选项为 5min、1hour、1day 注意：必须带 粒度前数字
freq = '1day'

# 区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
regions = [
    "china"
]

# ISP运营商，比如all(所有 ISP)，telecom(电信)，unicom(联通)，mobile(中国移动)，drpeng(鹏博士)，tietong(铁通)，cernet(教育网)
isp = "all"

# 开始时间，格式为：2006-01-02。起止最大间隔为31天
startDate = "2020-03-22"

# 结束时间，格式为：2006-01-02。起止最大间隔为31天
endDate = "2020-03-24"

ret, info = cdn_manager.get_loganalyze_bandwidth(domains, freq, regions, isp, startDate, endDate)

print(ret)
print(info)

"""3、批量查询状态码：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#6"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

# 域名列表，总数不超过100条
domains = [
    'q7l1lwj1m.bkt.clouddn.com'
]

# 粒度，可选项为 5min、1hour、1day 注意：必须带 粒度前数字
freq = '1day'

# 开始时间，格式为：2006-01-02。起止最大间隔为31天
startDate = "2020-03-22"

# 结束时间，格式为：2006-01-02。起止最大间隔为31天
endDate = "2020-03-24"

ret, info = cdn_manager.get_loganalyze_statuscode(domains, freq, startDate, endDate)

print(ret)
print(info)

"""4、批量查询命中率：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#7"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

# 域名列表，总数不超过100条
domains = [
    'q7l1lwj1m.bkt.clouddn.com'
]

# 粒度，可选项为 5min、1hour、1day 注意：必须带 粒度前数字
freq = '1day'

# 开始时间，格式为：2006-01-02。起止最大间隔为31天
startDate = "2020-03-22"

# 结束时间，格式为：2006-01-02。起止最大间隔为31天
endDate = "2020-03-24"

ret, info = cdn_manager.get_loganalyze_hitmiss(domains, freq, startDate, endDate)

print(ret)
print(info)

"""5、批量查询请求次数：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#8"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

# 域名列表，总数不超过100条
domains = [
    'q7l1lwj1m.bkt.clouddn.com'
]

# 粒度，可选项为 5min、1hour、1day 注意：必须带 粒度前数字
freq = '1day'

# 区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
region = "china"

# 开始时间，格式为：2006-01-02。起止最大间隔为31天
startDate = "2020-03-22"

# 结束时间，格式为：2006-01-02。起止最大间隔为31天
endDate = "2020-03-24"

ret, info = cdn_manager.get_loganalyze_reqcount(domains, freq, region, startDate, endDate)

print(ret)
print(info)

"""6、批量查询 ISP 请求次数：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#9"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

# 域名列表，总数不超过100条
domains = [
    'q7l1lwj1m.bkt.clouddn.com'
]

# 粒度，可选项为 5min、1hour、1day 注意：必须带 粒度前数字
freq = '1day'

# 区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
region = "china"

# 开始时间，格式为：2006-01-02。起止最大间隔为31天
startDate = "2020-03-22"

# 结束时间，格式为：2006-01-02。起止最大间隔为31天
endDate = "2020-03-24"

ret, info = cdn_manager.get_loganalyze_ispreqcount(domains, freq, region, startDate, endDate)

print(ret)
print(info)

"""7、批量查询 ISP 流量占比：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#10"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

# 域名列表，总数不超过100条
domains = [
    'q7l1lwj1m.bkt.clouddn.com'
]

# 区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
regions = ["china"]

# 开始时间，格式为：2006-01-02。起止最大间隔为31天
startDate = "2020-03-22"

# 结束时间，格式为：2006-01-02。起止最大间隔为31天
endDate = "2020-03-24"

ret, info = cdn_manager.get_loganalyze_isptraffic(domains, regions, startDate, endDate)

print(ret)
print(info)

"""8、批量请求访问次数 Top IP：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#11"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

# 域名列表，总数不超过100条
domains = [
    'q7l1lwj1m.bkt.clouddn.com'
]

# 区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
region = "china"

# 开始时间，格式为：2006-01-02。起止最大间隔为31天
startDate = "2020-03-22"

# 结束时间，格式为：2006-01-02。起止最大间隔为31天
endDate = "2020-03-24"

ret, info = cdn_manager.get_loganalyze_topcountip(domains, region, startDate, endDate)

print(ret)
print(info)

"""9、批量请求访问流量 Top IP：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#12"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

# 域名列表，总数不超过100条
domains = [
    'q7l1lwj1m.bkt.clouddn.com'
]

# 区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
region = "china"

# 开始时间，格式为：2006-01-02。起止最大间隔为31天
startDate = "2020-03-22"

# 结束时间，格式为：2006-01-02。起止最大间隔为31天
endDate = "2020-03-24"

ret, info = cdn_manager.get_loganalyze_topcountip(domains, region, startDate, endDate)

print(ret)
print(info)

"""10、批量请求访问次数 Top URL：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#13"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

# 域名列表，总数不超过100条
domains = [
    'q7l1lwj1m.bkt.clouddn.com'
]

# 区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
regions = "china"

# 开始时间，格式为：2006-01-02。起止最大间隔为31天
startDate = "2020-03-22"

# 结束时间，格式为：2006-01-02。起止最大间隔为31天
endDate = "2020-03-24"

ret, info = cdn_manager.get_loganalyze_topcounturl(domains, regions, startDate, endDate)

print(ret)
print(info)

"""11、批量请求访问流量 Top URL：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#14"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

# 域名列表，总数不超过100条
domains = [
    'q7l1lwj1m.bkt.clouddn.com'
]

# 区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
regions = "china"

# 开始时间，格式为：2006-01-02。起止最大间隔为31天
startDate = "2020-03-22"

# 结束时间，格式为：2006-01-02。起止最大间隔为31天
endDate = "2020-03-24"

ret, info = cdn_manager.get_loganalyze_toptrafficurl(domains, regions, startDate, endDate)

print(ret)
print(info)

"""12、批量查询 PageView：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#15"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

# 域名列表，总数不超过100条
domains = [
    'q7l1lwj1m.bkt.clouddn.com'
]

# 粒度，可选项为 1hour、1day 注意：必须带 粒度前数字
freq = '1day'

# 开始时间，格式为：2006-01-02。起止最大间隔为31天
startDate = "2020-03-22"

# 结束时间，格式为：2006-01-02。起止最大间隔为31天
endDate = "2020-03-24"

ret, info = cdn_manager.get_loganalyze_pageview(domains, freq, startDate, endDate)

print(ret)
print(info)

"""13、批量查询 UniqueVisitor：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#16"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

# 域名列表，总数不超过100条
domains = [
    'q7l1lwj1m.bkt.clouddn.com'
]

# 粒度，可选项为 1hour、1day 注意：必须带 粒度前数字
freq = '1day'

# 开始时间，格式为：2006-01-02。起止最大间隔为31天
startDate = "2020-03-22"

# 结束时间，格式为：2006-01-02。起止最大间隔为31天
endDate = "2020-03-24"

ret, info = cdn_manager.get_loganalyze_uniquevisitor(domains, freq, startDate, endDate)

print(ret)
print(info)
