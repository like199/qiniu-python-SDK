# -*- coding: utf-8 -*-

from qiniu import http
import json

from qiniu.compat import is_py2
from qiniu.compat import is_py3

import hashlib


def urlencode(str):
    if is_py2:
        import urllib2
        return urllib2.quote(str)
    elif is_py3:
        import urllib.parse
        return urllib.parse.quote(str)


class CdnManager(object):
    def __init__(self, auth):
        self.auth = auth
        self.server = 'http://fusion.qiniuapi.com'

    def refresh_urls(self, urls):
        """
        刷新文件列表，文档 http://developer.qiniu.com/article/fusion/api/refresh.html

        Args:
            urls: 待刷新的文件外链列表

        Returns:
            一个dict变量和一个ResponseInfo对象
            参考代码 examples/cdn_manager.py
        """
        return self.refresh_urls_and_dirs(urls, None)

    def refresh_dirs(self, dirs):
        """
        刷新目录，文档 http://developer.qiniu.com/article/fusion/api/refresh.html

        Args:
            urls: 待刷新的目录列表

        Returns:
            一个dict变量和一个ResponseInfo对象
            参考代码 examples/cdn_manager.py
        """
        return self.refresh_urls_and_dirs(None, dirs)

    def refresh_urls_and_dirs(self, urls, dirs):
        """
        刷新文件目录，文档 http://developer.qiniu.com/article/fusion/api/refresh.html

        Args:
           urls: 待刷新的目录列表
           dirs: 待刷新的文件列表

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
       """
        req = {}
        if urls is not None and len(urls) > 0:
            req.update({"urls": urls})
        if dirs is not None and len(dirs) > 0:
            req.update({"dirs": dirs})

        body = json.dumps(req)
        url = '{0}/v2/tune/refresh'.format(self.server)
        return self.__post(url, body)

    def prefetch_urls(self, urls):
        """
        预取文件列表，文档 http://developer.qiniu.com/article/fusion/api/prefetch.html

        Args:
           urls: 待预取的文件外链列表

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"urls": urls})

        body = json.dumps(req)
        url = '{0}/v2/tune/prefetch'.format(self.server)
        return self.__post(url, body)

    def get_bandwidth_data(self, domains, start_date, end_date, granularity):
        """
        查询带宽数据，文档 http://developer.qiniu.com/article/fusion/api/traffic-bandwidth.html

        Args:
           domains:     域名列表
           start_date:  起始日期
           end_date:    结束日期
           granularity: 数据间隔

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": ';'.join(domains)})
        req.update({"startDate": start_date})
        req.update({"endDate": end_date})
        req.update({"granularity": granularity})

        body = json.dumps(req)
        url = '{0}/v2/tune/bandwidth'.format(self.server)
        return self.__post(url, body)

    def get_dynreqcount_data(self, domains, start_date, end_date, granularity):
        """
        批量查询动态加速之动态请求数，文档 https://developer.qiniu.com/fusion/api/1230/traffic-bandwidth#5

        Args:
           domains:     域名列表
           start_date:  起始日期，例如：2016-07-01
           end_date:    结束日期，例如：2016-07-03
           granularity: 粒度，取值：5min ／ hour ／day

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": ';'.join(domains)})
        req.update({"startDate": start_date})
        req.update({"endDate": end_date})
        req.update({"granularity": granularity})

        body = json.dumps(req)
        url = '{0}/v2/tune/dynreqcount'.format(self.server)
        return self.__post(url, body)

    def get_cdn_top_url(self, domains, region, startDate, endDate):
        """
        批量请求访问次数Top URL，文档：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis
        Args:
           domains:    域名列表，总数不超过100条
           region:     区域，可选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
           startDate:  开始日期，格式为：2006-01-02。起止最大间隔为31天
           endDate:    结束时间，格式为：2006-01-02。起止最大间隔为31天
        :return:
        """
        req = {}
        req.update({"domains": domains})
        req.update({"region": region})
        req.update({"startDate": startDate})
        req.update({"endDate": endDate})

        body = json.dumps(req)
        url = '{0}/v2/tune/loganalyze/topcounturl'.format(self.server)
        return self.__post(url, body)

    def get_flux_data(self, domains, start_date, end_date, granularity):
        """
        查询流量数据，文档 http://developer.qiniu.com/article/fusion/api/traffic-bandwidth.html

        Args:
           domains:     域名列表
           start_date:  起始日期
           end_date:    结束日期
           granularity: 数据间隔

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": ';'.join(domains)})
        req.update({"startDate": start_date})
        req.update({"endDate": end_date})
        req.update({"granularity": granularity})

        body = json.dumps(req)
        url = '{0}/v2/tune/flux'.format(self.server)
        return self.__post(url, body)

    def get_log_list_data(self, domains, log_date):
        """
        获取日志下载链接，文档 http://developer.qiniu.com/article/fusion/api/log.html

        Args:
           domains:     域名列表
           log_date:    日志日期

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": ';'.join(domains)})
        req.update({"day": log_date})

        body = json.dumps(req)
        url = '{0}/v2/tune/log/list'.format(self.server)
        return self.__post(url, body)

    def get_loganalyze_traffic(self, domains, freq, regions, isp, startDate, endDate):
        """
        获取区域运营商流量查询，文档 https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#4

        Args:
           domains:     域名列表，总数不超过100条
           freq:    	粒度，可选项为 5min、1hour、1day
           regions:     区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
           isp：        ISP运营商，比如all(所有 ISP)，telecom(电信)，unicom(联通)，mobile(中国移动)，drpeng(鹏博士)，tietong(铁通)，cernet(教育网)
           startDate：  开始时间，格式为：2006-01-02。起止最大间隔为31天
           endDate：    结束时间，格式为：2006-01-02。起止最大间隔为31天

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": domains})
        req.update({"freq": freq})
        req.update({"regions": regions})
        req.update({"isp": isp})
        req.update({"startDate": startDate})
        req.update({"endDate": endDate})

        body = json.dumps(req)
        url = '{0}/v2/tune/loganalyze/traffic'.format(self.server)
        return self.__post(url, body)

    def get_loganalyze_bandwidth(self, domains, freq, regions, isp, startDate, endDate):
        """
        获取区域运营商带宽查询，文档 https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#5

        Args:
           domains:     域名列表，总数不超过100条
           freq:    	粒度，可选项为 5min、1hour、1day
           regions:     区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
           isp：        ISP运营商，比如all(所有 ISP)，telecom(电信)，unicom(联通)，mobile(中国移动)，drpeng(鹏博士)，tietong(铁通)，cernet(教育网)
           startDate：  开始时间，格式为：2006-01-02。起止最大间隔为31天
           endDate：    结束时间，格式为：2006-01-02。起止最大间隔为31天

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": domains})
        req.update({"freq": freq})
        req.update({"regions": regions})
        req.update({"isp": isp})
        req.update({"startDate": startDate})
        req.update({"endDate": endDate})

        body = json.dumps(req)
        url = '{0}/v2/tune/loganalyze/bandwidth'.format(self.server)
        return self.__post(url, body)

    def get_loganalyze_statuscode(self, domains, freq, startDate, endDate):
        """
        批量查询状态码，文档 https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#6

        Args:
           domains:     域名列表，总数不超过100条
           freq:    	粒度，可选项为 5min、1hour、1day
           startDate：  开始时间，格式为：2006-01-02。起止最大间隔为31天
           endDate：    结束时间，格式为：2006-01-02。起止最大间隔为31天

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": domains})
        req.update({"freq": freq})
        req.update({"startDate": startDate})
        req.update({"endDate": endDate})

        body = json.dumps(req)
        url = '{0}/v2/tune/loganalyze/statuscode'.format(self.server)
        return self.__post(url, body)

    def get_loganalyze_hitmiss(self, domains, freq, startDate, endDate):
        """
        批量查询命中率，文档 https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#7

        Args:
           domains:     域名列表，总数不超过100条
           freq:    	粒度，可选项为 5min、1hour、1day
           startDate：  开始时间，格式为：2006-01-02。起止最大间隔为31天
           endDate：    结束时间，格式为：2006-01-02。起止最大间隔为31天

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": domains})
        req.update({"freq": freq})
        req.update({"startDate": startDate})
        req.update({"endDate": endDate})

        body = json.dumps(req)
        url = '{0}/v2/tune/loganalyze/hitmiss'.format(self.server)
        return self.__post(url, body)

    def get_loganalyze_reqcount(self, domains, freq, region, startDate, endDate):
        """
        批量查询请求次数，文档 https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#8

        Args:
           domains:     域名列表，总数不超过100条
           freq:    	粒度，可选项为 5min、1hour、1day
           region:      区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
           startDate：  开始时间，格式为：2006-01-02。起止最大间隔为31天
           endDate：    结束时间，格式为：2006-01-02。起止最大间隔为31天

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": domains})
        req.update({"freq": freq})
        req.update({"region": region})
        req.update({"startDate": startDate})
        req.update({"endDate": endDate})

        body = json.dumps(req)
        url = '{0}/v2/tune/loganalyze/reqcount'.format(self.server)
        return self.__post(url, body)

    def get_loganalyze_ispreqcount(self, domains, freq, region, startDate, endDate):
        """
        批量查询 ISP 请求次数，文档 https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#9

        Args:
           domains:     域名列表，总数不超过100条
           freq:    	粒度，可选项为 5min、1hour、1day
           region:      区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
           startDate：  开始时间，格式为：2006-01-02。起止最大间隔为31天
           endDate：    结束时间，格式为：2006-01-02。起止最大间隔为31天

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": domains})
        req.update({"freq": freq})
        req.update({"region": region})
        req.update({"startDate": startDate})
        req.update({"endDate": endDate})

        body = json.dumps(req)
        url = '{0}/v2/tune/loganalyze/ispreqcount'.format(self.server)
        return self.__post(url, body)

    def get_loganalyze_isptraffic(self, domains, regions, startDate, endDate):
        """
        批量查询 ISP 流量占比，文档 https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#10

        Args:
           domains:     域名列表，总数不超过100条
           regions:      区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
           startDate：  开始时间，格式为：2006-01-02。起止最大间隔为31天
           endDate：    结束时间，格式为：2006-01-02。起止最大间隔为31天

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": domains})
        req.update({"regions": regions})
        req.update({"startDate": startDate})
        req.update({"endDate": endDate})

        body = json.dumps(req)
        url = '{0}/v2/tune/loganalyze/isptraffic'.format(self.server)
        return self.__post(url, body)

    def get_loganalyze_topcountip(self, domains, region, startDate, endDate):
        """
        批量请求访问次数 Top IP，文档 https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#11

        Args:
           domains:     域名列表，总数不超过100条
           region:      区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
           startDate：  开始时间，格式为：2006-01-02。起止最大间隔为31天
           endDate：    结束时间，格式为：2006-01-02。起止最大间隔为31天

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": domains})
        req.update({"region": region})
        req.update({"startDate": startDate})
        req.update({"endDate": endDate})

        body = json.dumps(req)
        url = '{0}/v2/tune/loganalyze/topcountip'.format(self.server)
        return self.__post(url, body)

    def get_loganalyze_toptrafficip(self, domains, region, startDate, endDate):
        """
        批量请求访问流量 Top IP，文档 https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#12

        Args:
           domains:     域名列表，总数不超过100条
           region:      区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
           startDate：  开始时间，格式为：2006-01-02。起止最大间隔为31天
           endDate：    结束时间，格式为：2006-01-02。起止最大间隔为31天

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": domains})
        req.update({"region": region})
        req.update({"startDate": startDate})
        req.update({"endDate": endDate})

        body = json.dumps(req)
        url = '{0}/v2/tune/loganalyze/toptrafficip'.format(self.server)
        return self.__post(url, body)

    def get_loganalyze_topcounturl(self, domains, region, startDate, endDate):
        """
        批量请求访问次数 Top URL，文档 https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#13

        Args:
           domains:     域名列表，总数不超过100条
           region:      区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
           startDate：  开始时间，格式为：2006-01-02。起止最大间隔为31天
           endDate：    结束时间，格式为：2006-01-02。起止最大间隔为31天

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": domains})
        req.update({"region": region})
        req.update({"startDate": startDate})
        req.update({"endDate": endDate})

        body = json.dumps(req)
        url = '{0}/v2/tune/loganalyze/topcounturl'.format(self.server)
        return self.__post(url, body)

    def get_loganalyze_toptrafficurl(self, domains, region, startDate, endDate):
        """
        批量请求访问流量 Top URL，文档 https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#14

        Args:
           domains:     域名列表，总数不超过100条
           region:      区域，选项见 Region 参数列表：https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#region
           startDate：  开始时间，格式为：2006-01-02。起止最大间隔为31天
           endDate：    结束时间，格式为：2006-01-02。起止最大间隔为31天

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": domains})
        req.update({"region": region})
        req.update({"startDate": startDate})
        req.update({"endDate": endDate})

        body = json.dumps(req)
        url = '{0}/v2/tune/loganalyze/toptrafficurl'.format(self.server)
        return self.__post(url, body)

    def get_loganalyze_pageview(self, domains, freq, startDate, endDate):
        """
        批量查询 PageView，文档 https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#15

        Args:
           domains:     域名列表，总数不超过100条
           freq:    	粒度，可选项为 1hour、1day
           startDate：  开始时间，格式为：2006-01-02。起止最大间隔为31天
           endDate：    结束时间，格式为：2006-01-02。起止最大间隔为31天

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": domains})
        req.update({"freq": freq})
        req.update({"startDate": startDate})
        req.update({"endDate": endDate})

        body = json.dumps(req)
        url = '{0}/v2/tune/loganalyze/pageview'.format(self.server)
        return self.__post(url, body)

    def get_loganalyze_uniquevisitor(self, domains, freq, startDate, endDate):
        """
        批量查询 UniqueVisitor，文档 https://developer.qiniu.com/fusion/api/4081/cdn-log-analysis#16

        Args:
           domains:     域名列表，总数不超过100条
           freq:    	粒度，可选项为 1hour、1day
           startDate：  开始时间，格式为：2006-01-02。起止最大间隔为31天
           endDate：    结束时间，格式为：2006-01-02。起止最大间隔为31天

        Returns:
           一个dict变量和一个ResponseInfo对象
           参考代码 examples/cdn_manager.py
        """
        req = {}
        req.update({"domains": domains})
        req.update({"freq": freq})
        req.update({"startDate": startDate})
        req.update({"endDate": endDate})

        body = json.dumps(req)
        url = '{0}/v2/tune/loganalyze/uniquevisitor'.format(self.server)
        return self.__post(url, body)

    def put_httpsconf(self, name, certid, forceHttps=False):
        """
        修改证书，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#11

        Args:
           domains:     域名name
           CertID:      证书id，从上传或者获取证书列表里拿到证书id
           ForceHttps:  是否强制https跳转

        Returns:
           {}
        """
        req = {}
        req.update({"certid": certid})
        req.update({"forceHttps": forceHttps})

        body = json.dumps(req)
        url = '{0}/domain/{1}/httpsconf'.format(self.server, name)
        return self.__post(url, body)

    def __post(self, url, data=None):
        headers = {'Content-Type': 'application/json'}
        return http._post_with_auth_and_headers(url, data, self.auth, headers)


class DomainManager(object):
    def __init__(self, auth):
        self.auth = auth
        self.server = 'http://api.qiniu.com'

    def create_domain(self, name, body):
        """
        创建域名，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name

        Args:
           name:     域名, 如果是泛域名，必须以点号 . 开头
           bosy:     创建域名参数
        Returns:
           {}
        """
        url = '{0}/domain/{1}'.format(self.server, name)
        return self.__post(url, body)

    def domain_online(self, name):
        """
        上线域名，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#6

        Args:
            name:     域名, 如果是泛域名，必须以点号 . 开头
            bosy:     创建域名参数
        Returns:
            {}
        """
        url = '{0}/domain/{1}/online'.format(self.server, name)
        return http._post_with_qiniu_mac(url, None, self.auth)

    def domain_offline(self, name):
        """
        下线域名，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#5

        Args:
            name:     域名, 如果是泛域名，必须以点号 . 开头
            bosy:     创建域名参数
        Returns:
            {}
        """
        url = '{0}/domain/{1}/offline'.format(self.server, name)
        return http._post_with_qiniu_mac(url, None, self.auth)

    def delete_domain(self, name):
        """
        删除域名，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#8

        Args:
            name:     域名, 如果是泛域名，必须以点号 . 开头
        Returns:
            返回一个tuple对象，其格式为(<result>, <ResponseInfo>)
            - result          成功返回dict{}，失败返回{"error": "<errMsg string>"}
            - ResponseInfo    请求的Response信息
        """
        url = '{0}/domain/{1}'.format(self.server, name)
        return self.__get(url)

    def get_domain(self, name):
        """
        获取域名信息，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name

        Args:
           name:     域名, 如果是泛域名，必须以点号 . 开头
        Returns:
            返回一个tuple对象，其格式为(<result>, <ResponseInfo>)
            - result          成功返回dict{}，失败返回{"error": "<errMsg string>"}
            - ResponseInfo    请求的Response信息
        """
        url = '{0}/domain/{1}'.format(self.server, name)
        return self.__get(url)

    def get_domainList(self, marker, limit):
        """
        获取域名列表，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#9

        Args:
           marker:     用于标示从哪个位置开始获取域名列表。不填或空表示从头开始
           limit:      返回的最大域名个数。1~1000, 不填默认为 10
        Returns:
            返回一个tuple对象，其格式为(<result>, <ResponseInfo>)
            - result          成功返回dict{}，失败返回{"error": "<errMsg string>"}
            - ResponseInfo    请求的Response信息
        """
        if marker is None or marker == "" and limit == "":
            limit = 10
            url = '{0}/domain?limit={1}'.format(self.server, limit)
        else:
            url = '{0}/domain?marker={1}&limit={2}'.format(self.server, marker, limit)
        return self.__get(url)

    def https_sslize(self, name, certid, forceHttps=False, http2Enable=False):
        """
        https降级，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#11

        Args:
            domains:     域名name
            CertID:      证书id，从上传或者获取证书列表里拿到证书id
            ForceHttps:  是否强制https跳转

        Returns:
            {}
        """
        req = {}
        req.update({"certid": certid})
        req.update({"forceHttps": forceHttps})
        req.update({"http2Enable": http2Enable})
        body = json.dumps(req)
        url = '{0}/domain/{1}/sslize'.format(self.server, name)
        return self.__put(url, body)

    def https_unsslize(self, name):
        """
        https降级，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#11

        Args:
            domains:     域名name
            CertID:      证书id，从上传或者获取证书列表里拿到证书id
            ForceHttps:  是否强制https跳转

        Returns:
            {}
        """
        url = '{0}/domain/{1}/unsslize'.format(self.server, name)
        return http._put_with_qiniu_mac(url, None, self.auth)

    def put_httpsconf(self, name, certid, forceHttps=False, http2Enable=False):
        """
        修改证书，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#11

        Args:
           domains:     域名name
           CertID:      证书id，从上传或者获取证书列表里拿到证书id
           ForceHttps:  是否强制https跳转

        Returns:
           {}
        """
        req = {}
        req.update({"certid": certid})
        req.update({"forceHttps": forceHttps})
        req.update({"http2Enable": http2Enable})
        body = json.dumps(req)
        url = '{0}/domain/{1}/httpsconf'.format(self.server, name)
        return self.__put(url, body)

    def put_referer(self, name, refererType, refererValues, nullReferer=False):
        """
        修改referer防盗链，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#13

        Args:
            name:               域名, 如果是泛域名，必须以点号 . 开头
            refererType:        Referer防盗链类型： black/white
            refererValues:      Referer防盗链黑白名单,列表格式
            nullReferer:        Referer防盗链, 是否支持空referer，不填为false

        Returns:
           {}
        """
        req = {}
        req.update({"refererType": refererType})
        req.update({"refererValues": refererValues})
        req.update({"nullReferer": nullReferer})
        body = json.dumps(req)
        url = '{0}/domain/{1}/referer'.format(self.server, name)
        return self.__put(url, body)

    def put_ipacl(self, name, ipACLType, ipACLValues):
        """
        修改IP黑白名单，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#14

        Args:
            name:             域名, 如果是泛域名，必须以点号 . 开头
            ipACLType:        ip黑白名单控制控制类型, black/white
            ipACLValues:      ip黑白名单，列表格式，ip格式为：127.0.0.1/24

        Returns:
           {}
        """
        req = {}
        req.update({"ipACLType": ipACLType})
        req.update({"ipACLValues": ipACLValues})
        body = json.dumps(req)
        url = '{0}/domain/{1}/ipacl'.format(self.server, name)
        return self.__put(url, body)

    def put_timeacl(self, name, timeACLKeys, checkUrl, enable=False):
        """
        修改时间戳防盗链，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#13

        Args:
            name:               域名, 如果是泛域名，必须以点号 . 开头
            enable:             开启时间戳防盗链的开关，默认为false
            timeACLKeys:        时间戳防盗链的加密key，该key字符长区间为[24,40]，Enable为true时timeACLKeys必填2个key,Enable为false时 timeACLKeys不填
            checkUrl:           根据时间戳防盗链加密算法生成的url，timeACL为true时本项必填, 用以验证是否真实了解该时间戳防盗链加密算法
        Returns:
           {}
        """
        req = {}
        if enable == False:
            timeACLKeys = None
            checkUrl = None
            req.update({"enable": enable})
            req.update({"timeACLKeys": timeACLKeys})
            req.update({"checkUrl": checkUrl})
        else:
            try:
                if 24 <= len(timeACLKeys[0]) <= 40 and 24 <= len(timeACLKeys[1]) <= 40:
                    timeACLKeys = [timeACLKeys[0], timeACLKeys[1]]
                    req.update({"timeACLKeys": timeACLKeys})
                elif len(timeACLKeys[0]) > 40 or len(timeACLKeys[1]) > 40:
                    timeACLKeys = [timeACLKeys[0][0:40], timeACLKeys[1][0:40]]
                req.update({"enable": enable})
                req.update({"checkUrl": checkUrl})
            except Exception as e:
                return None, ResponseInfo(None, e)
        body = json.dumps(req)
        url = '{0}/domain/{1}/timeacl'.format(self.server, name)
        return self.__put(url, body)

    def put_cache(self, name, cacheControls, ignoreParam=False):
        """
        修改缓存配置，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#4

        Args:
            cacheControls:[
                {
                    time:       缓存时间，注意不论哪种时间单位，总时间都不能超过1年,type为follow，本字段配为 -1
                    timeunit:   缓存时间单位：0(秒)/1(分钟)/2(小时)/3(天)/4(周)/5(月)/6(年)，type为follow，本字段配为0
                    type:       缓存类型：all(默认全局规则)/path(路径匹配)/suffix(后缀匹配)/follow(遵循源站)
                    rule:       缓存路径规则：以分号;分割的字符串，每个里面类型一致，比如CCType为path的话，这里每个分号分割的都是以/开头，suffix的话，以点号.开头，如果是all类型，或者follow，统一只要填一个星号*
                },
                {
                    ...
                }
            ]
            ignoreParam: 是否开启去问号缓存，默认为false
        Returns:
           {}
        """
        req = {}
        req.update({"cacheControls": cacheControls})
        req.update({"ignoreParam": ignoreParam})
        body = json.dumps(req)
        url = '{0}/domain/{1}/cache'.format(self.server, name)
        return self.__put(url, body)

    def put_source(self, name, sourceType, data, sourceHost=None):
        """
        修改源站，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#3

        Args:
            sourceType:         源站类型: domain(域名)/ip(ip地址)/qiniuBucket(七牛云存储，备注：不支持平台是动态加速)/advanced(高级)
            sourceHost:         回源Host, 普通域名默认SourceHost为域名本身，泛域名默认SourceHost为用户请求时的域名
            sourceIPs:          回源ip, sourceType为ip时sourceIPs必填
            sourceDomain:       回源域名, sourceType为domain时此字段必填
            sourceQiniuBucket:  回源的七牛云存储的bucket名称, sourceType为qiniuBucket时此字段必填
            sourceURLScheme:    回源协议, 仅用于https域名，可选值: http/https, 回源七牛bucket时本值无效,默认不填是follow请求协议
            advancedSources: [
                {
                    addr:       高级回源的回源地址, 可以是IP或者域名, sourceType为advanced时advancedSources字段必填
                    weight:     高级回源的回源addr权重, 1 ~ 65535, 按照权重比例回源，sourceType为advanced时advancedSources字段必填
                    backup:     高级回源的回源addr是否为备源地址，sourceType为advanced时advancedSources字段必填
                }
            ],
            testURLPath:        用于测试的URL Path, 检测源站是否可访问, 大小建议小于1KB，采用静态资源，并请不要删除, 后面域名任何配置更改都会测试该资源, 用以保证域名的访问性
        Returns:
           {}
        """
        req = {}
        try:
            if sourceType == "0":
                req.update({"sourceType": "domain"})
                try:
                    if data["sourceDomain"] is not None and data["testURLPath"] is not None:
                        req.update({"sourceDomain": data["sourceDomain"]})
                except Exception as e:
                    return None, http.ResponseInfo(None, e)
            elif sourceType == "1":
                req.update({"sourceType": "ip"})
                try:
                    if data["sourceIPs"] is not None and data["testURLPath"] is not None:
                        req.update({"sourceIPs": data["sourceIPs"]})
                except Exception as e:
                    return None, http.ResponseInfo(None, e)
            elif sourceType == "2":
                req.update({"sourceType": "qiniuBucket"})
                try:
                    if data["sourceQiniuBucket"] is not None and data["testURLPath"] is not None:
                        req.update({"sourceQiniuBucket": data["sourceQiniuBucket"]})
                except Exception as e:
                    return None, http.ResponseInfo(None, e)
            elif sourceType == "3":
                req.update({"sourceType": "advanced"})
                try:
                    if data["sourceQiniuBucket"] is not None and data["testURLPath"] is not None:
                        req.update({"advancedSources": data["advancedSources"]})
                except Exception as e:
                    return None, http.ResponseInfo(None, e)
            req.update({"testURLPath": data["testURLPath"]})
            if sourceHost is None or sourceHost == "":
                req.update({"sourceHost": name})
            else:
                req.update({"sourceHost": sourceHost})
        except Exception as e:
            return None, http.ResponseInfo(None, e)
        body = json.dumps(req)
        url = '{0}/domain/{1}/source'.format(self.server, name)
        return self.__put(url, body)

    def put_bsauth(self, name, isQiniuPrivate, enable, data=None):
        """
        修改回源鉴权，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#16

        Args:
            isQiniuPrivate:<IsQiniuPrivate>,            是否为七牛私有bucket鉴权，如果是七牛私有bucket，只需要打开 enable开关，本功能将随着回源鉴权功能使能
            enable: <Enable>,	                        回源鉴权开关
            data:{
                注意：如果是 七牛私有bucket鉴权，以下参数不需要填
                path: [<Path>, ...],                    要匹配这个回源鉴权的path，目前该功能还不支持
                method: <Method>,                       回源鉴权支持的http方法，GET/POST/HEAD
                parameters: [<Parameter>, ...],         回源鉴权中参与鉴权的url 参数，取值取决于用户鉴权服务器的鉴权规则
                timeLimit: <TimeLimit>,                 回源鉴权的鉴权超时时间，单位ms, 最小 100ms(0.1s), 最大10000ms(10s)
                userAuthUrl: <UserAuthUrl>,             回源鉴权: 用户鉴权的鉴权服务地址
                strict: <Strict>,                       回源鉴权: 超时后，是否严格为鉴权失败
                successStatusCode: <SuccessStatusCode>, 回源鉴权: 鉴权通过的http code, 最小100，最大10000
                failureStatusCode: <FailureStatusCode>  回源鉴权: 鉴权失败的http code, 最小100，最大10000
            }
        Returns:
            {}
        """
        req = {}
        try:
            if isQiniuPrivate is True and enable is True and data is None:
                req.update({"isQiniuPrivate": isQiniuPrivate})
                req.update({"enable": enable})
            elif isQiniuPrivate is False and enable is True and data is not None:
                req.update({"method": data["method"]})
                req.update({"timeLimit": data["timeLimit"]})
                req.update({"userAuthUrl": data["userAuthUrl"]})
                req.update({"successStatusCode": data["successStatusCode"]})
                req.update({"failureStatusCode": data["failureStatusCode"]})
                req.update({"Strict": data["Strict"]})
                req.update({"parameters": data["parameters"]})
            elif isQiniuPrivate is False and enable is False and data is None:
                req.update({"isQiniuPrivate": isQiniuPrivate})
                req.update({"enable": isQiniuPrivate})
            else:
                print("参数设置不对，请先核实参数！")
        except Exception as e:
            return None, http.ResponseInfo(None, e)
        body = json.dumps(req)
        url = '{0}/domain/{1}/bsauth'.format(self.server, name)
        return self.__put(url, body)

    def put_external(self, name, enableFop=False, data=None):
        """
        修改特殊配置，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#17

        Args:
            enableFop: <EnableFop>,                          是否自动开启七牛fop图片处理（备注：不支持平台是动态加速）
            imageSlim:{
                enableImageSlim: <EnableImageSlim>,           是否自动开启图片瘦身（备注：不支持平台是动态加速）
                prefixImageSlims: [<PrefixImageSlim>,...]，   图片瘦身匹配的指定目录, 例如/abc
                regexpImageSlims: [<RegexpImageSlim>,...]     图片瘦身匹配的指定的正则表达式, 例如.*png
            }
        Returns:
            {}
        """
        req = {}
        req.update({"enableFop": enableFop})
        req.update({"imageSlim": data})
        body = json.dumps(req)
        url = '{0}/domain/{1}/external'.format(self.server, name)
        return self.__put(url, body)

    def create_sslcert(self, name, common_name, pri, ca):
        """
        上传证书，文档 https://developer.qiniu.com/fusion/api/4246/the-domain-name#11

        Args:
           name:        证书名称
           common_name: 相关域名
           pri:         证书私钥
           ca:          证书内容
        Returns:
            返回一个tuple对象，其格式为(<result>, <ResponseInfo>)
            - result          成功返回dict{certID: <CertID>}，失败返回{"error": "<errMsg string>"}
            - ResponseInfo    请求的Response信息


        """
        req = {}
        req.update({"name": name})
        req.update({"common_name": common_name})
        req.update({"pri": pri})
        req.update({"ca": ca})

        body = json.dumps(req)
        url = '{0}/sslcert'.format(self.server)
        return self.__post(url, body)

    def delete_sslcert(self, certid):
        """
        删除证书，文档：https://developer.qiniu.com/fusion/api/4248/certificate#2

        Args:
           certid:        证书ID
        Returns:
            {}
        """
        url = '{0}/sslcert/{1}'.format(self.server, certid)
        return self.__delete(url)

    def get_sslcertList(self, marker, limit):
        """
        获取证书列表，文档 https://developer.qiniu.com/fusion/api/4248/certificate#4

        Args:
           marker:     用于标示从哪个位置开始获取证书列表。不填或空表示从头开始
           limit:      返回的最大域名个数。默认 100
        Returns:
            返回一个tuple对象，其格式为(<result>, <ResponseInfo>)
            - result          成功返回dict{}，失败返回{"error": "<errMsg string>"}
            - ResponseInfo    请求的Response信息
        """
        if marker is None or marker == "" and limit == "":
            limit = 100
            url = '{0}/sslcert?limit={1}'.format(self.server, limit)
        else:
            url = '{0}/sslcert?marker={1}&limit={2}'.format(self.server, marker, limit)
        return self.__get(url)

    def get_sslcert(self, certid):
        """
        获取证书信息，文档 https://developer.qiniu.com/fusion/api/4248/certificate#3

        Args:
           certid:     证书ID
        Returns:
            返回一个tuple对象，其格式为(<result>, <ResponseInfo>)
            - result          成功返回dict{}，失败返回{"error": "<errMsg string>"}
            - ResponseInfo    请求的Response信息
        """
        url = '{0}/sslcert/{1}'.format(self.server, certid)
        return self.__get(url)

    def __get(self, url):
        return http._get_with_qiniu_mac(url, None, self.auth)

    def __post(self, url, data=None):
        headers = {'Content-Type': 'application/json'}
        return http._post_with_auth_and_headers(url, data, self.auth, headers)

    def __put(self, url, data=None):
        headers = {'Content-Type': 'application/json'}
        return http._put_with_auth_and_headers(url, data, self.auth, headers)

    def __delete(self, url):
        return http._delete_with_qiniu_mac(url, None, self.auth)


def create_timestamp_anti_leech_url(host, file_name, query_string, encrypt_key, deadline):
    """
    创建时间戳防盗链

    Args:
        host:              带访问协议的域名
        file_name:         原始文件名，不需要urlencode
        query_string:      查询参数，不需要urlencode
        encrypt_key:       时间戳防盗链密钥
        deadline:          链接有效期时间戳（以秒为单位）

    Returns:
        带时间戳防盗链鉴权访问链接
    """
    if query_string:
        url_to_sign = '{0}/{1}?{2}'.format(host, urlencode(file_name), query_string)
    else:
        url_to_sign = '{0}/{1}'.format(host, urlencode(file_name))

    path = '/{0}'.format(urlencode(file_name))
    expire_hex = str(hex(deadline))[2:]
    str_to_sign = '{0}{1}{2}'.format(encrypt_key, path, expire_hex).encode()
    sign_str = hashlib.md5(str_to_sign).hexdigest()

    if query_string:
        signed_url = '{0}&sign={1}&t={2}'.format(url_to_sign, sign_str, expire_hex)
    else:
        signed_url = '{0}?sign={1}&t={2}'.format(url_to_sign, sign_str, expire_hex)

    return signed_url
