# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, DomainManager
import json, time
from qiniu.services.cdn.manager import create_timestamp_anti_leech_url

"""获取域名列表"""
# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

manager = DomainManager(auth)

# 用于标示从哪个位置开始获取域名列表。不填或空表示从头开始
marker = ""

# 返回的最大域名个数。1~1000, 不填默认为 10
limit = ""

ret, res = manager.get_domainList(marker, limit)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""查询域名信息"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

manager = DomainManager(auth)

# 域名
name = ""

ret, res = manager.get_domain(name)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""删除域名"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

manager = DomainManager(auth)

# 域名
name = ""

ret, res = manager.delete_domain(name)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""域名上线"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

manager = DomainManager(auth)

# 域名
name = "zhuchangzhao2.peterpy.cn"

ret, res = manager.domain_online(name)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""域名下线"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

manager = DomainManager(auth)

# 域名
name = ""

ret, res = manager.domain_offline(name)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""https降级"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

manager = DomainManager(auth)

# 域名
name = ""

ret, res = manager.https_unsslize(name)

headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))

"""删除证书"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

manager = DomainManager(auth)

# 证书ID
certid = ""

ret, info = manager.delete_sslcert(certid)
print(info)

"""获取证书列表"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

manager = DomainManager(auth)

# 用于标示从哪个位置开始获取证书列表。不填或空表示从头开始
marker = ""

# 返回的最大域名个数。默认 100
limit = ""

ret, info = manager.get_domainList(marker, limit)
print(info)

"""获取单个证书"""

# AK、SK
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = QiniuMacAuth(access_key, secret_key)

manager = DomainManager(auth)

# 证书ID
certid = ""

ret, info = manager.get_sslcert(certid)
print(info)

"""上传证书"""

import qiniu
from qiniu import DomainManager

# 账户ak，sk
access_key = ''
secret_key = ''

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
domain_manager = DomainManager(auth)

privatekey = "ssl/www.qiniu.com/privkey.pem"
ca = "ssl/www.qiniu.com/fullchain.pem"
domain_name = 'www.qiniu.com'

with open(privatekey, 'r') as f:
    privatekey_str = f.read()

with open(ca, 'r') as f:
    ca_str = f.read()

ret, info = domain_manager.create_sslcert(
    domain_name, domain_name, privatekey_str, ca_str)
print(ret['certID'])

"""修改证书"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
domain_manager = DomainManager(auth)

privatekey = "ssl/www.qiniu.com/privkey.pem"
ca = "ssl/www.qiniu.com/fullchain.pem"
domain_name = 'www.qiniu.com'

with open(privatekey, 'r') as f:
    privatekey_str = f.read()

with open(ca, 'r') as f:
    ca_str = f.read()

# bool类型；是否强制https跳转，默认为false
forceHttps = False

# bool类型；http2功能是否启用，false为关闭，true为开启
http2Enable = False

ret, info = domain_manager.create_sslcert(
    domain_name, domain_name, privatekey_str, ca_str)

ret, info = domain_manager.put_httpsconf(domain_name, ret['certID'], forceHttps, http2Enable)
print(info)

"""http升级为https"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
domain_manager = DomainManager(auth)

# bool类型；是否强制https跳转，默认为false
forceHttps = False

# bool类型；http2功能是否启用，false为关闭，true为开启
http2Enable = False

ret, info = domain_manager.get_sslcertList()

ret, info = domain_manager.put_httpsconf(domain_name, ret['certs'][0], forceHttps, http2Enable)
print(info)

"""修改referer防盗链"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
domain_manager = DomainManager(auth)

# 域名, 如果是泛域名，必须以点号 . 开头
name = ""

# Referer防盗链类型： black/white
refererType = "black"

# Referer防盗链黑白名单，列表格式
refererValues = []

# Referer防盗链, 是否支持空referer，不填为false
nullReferer = False

ret, info = domain_manager.put_referer(name, refererType, refererValues, nullReferer)
print(info)

"""修改IP黑白名单"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
domain_manager = DomainManager(auth)

# 域名, 如果是泛域名，必须以点号 . 开头
name = ""

# ip黑白名单控制控制类型, black/white
ipACLType = "black"

# ip黑白名单，列表格式，ip格式为：127.0.0.1/24
ipACLValues = []

ret, info = domain_manager.put_ipacl(name, ipACLType, ipACLValues)
print(info)

"""修改时间戳防盗链"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
domain_manager = DomainManager(auth)

# 域名, 如果是泛域名，必须以点号 . 开头
name = ""

# 开启时间戳防盗链的开关，默认为false
enable = False

# 时间戳防盗链的加密key，该key字符长区间为[24,40]，Enable为true时timeACLKeys必填2个key,Enable为false时 timeACLKeys不填
timeACLKeys = []

# 根据时间戳防盗链加密算法生成的url，timeACL为true时本项必填, 用以验证是否真实了解该时间戳防盗链加密算法

host = 'http://{0}'.format(name)

# 配置时间戳时指定的key
encrypt_key = ''

# 资源路径
file_name = 'a/b/c/example.jpeg'

# 查询字符串,不需加?
query_string = timeACLKeys[0]

# 截止日期的时间戳,秒为单位，3600为当前时间一小时之后过期
deadline = int(time.time()) + 3600

checkUrl = create_timestamp_anti_leech_url(host, file_name, query_string, encrypt_key, deadline)

ret, info = domain_manager.put_timeacl(name, timeACLKeys, checkUrl, enable=enable)
print(info)

"""修改缓存配置"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = DomainManager(auth)

# 域名
name = ""

# 缓存规则
cacheControls = [
    {
        # 缓存时间，注意不论哪种时间单位，总时间都不能超过1年,type为follow，本字段配为 -1
        "time": "0",
        # 缓存时间单位：0(秒)/1(分钟)/2(小时)/3(天)/4(周)/5(月)/6(年)，type为follow，本字段配为0
        "timeunit": "0",
        # 缓存类型：all(默认全局规则)/path(路径匹配)/suffix(后缀匹配)/follow(遵循源站)
        "type": "suffix",
        # 缓存路径规则：以分号;分割的字符串，每个里面类型一致，比如CCType为path的话，这里每个分号分割的都是以/开头，suffix的话，以点号.开头，如果是all类型，或者follow，统一只要填一个星号*
        "rule": ".m3u8;.js"
    },
    {
        "time": 1,
        "timeunit": 5,
        "type": "all",
        "rule": "*"
    }
]

# 是否开启去问号缓存，默认为false
ignoreParam = False

ret, info = cdn_manager.put_cache(name, cacheControls, ignoreParam)

print(ret)
print(info)

"""修改源站：https://developer.qiniu.com/fusion/api/4246/the-domain-name#3"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = DomainManager(auth)

# 域名
name = "zhuchangzhao2.peterpy.cn"

# 回源Host, 不填或为None时为 普通域名默认SourceHost为域名本身，泛域名默认SourceHost为用户请求时的域名
sourceHost = ""

# 源站类型: 0 domain(域名)；1 ip(ip地址)；2 qiniuBucket(七牛云存储，备注：不支持平台是动态加速) 3 advanced(高级)
sourceType = "2"

"""
回源配置 字典格式传递
0 domain(域名)：必填 sourceDomain，testURLPath
1 ip(ip地址)：必填 sourceIPs 列表格式，testURLPath
2 qiniuBucket(七牛云存储，备注：不支持平台是动态加速)：必填 sourceQiniuBucket，testURLPath 
3 advanced(高级)：必填 advancedSources，testURLPath
advancedSources:[
{
    addr: <ASAddr>,      高级回源的回源地址, 可以是IP或者域名, sourceType为advanced时advancedSources字段必填
    weight: <ASWeight>,  高级回源的回源addr权重, 1 ~ 65535, 按照权重比例回源，sourceType为advanced时advancedSources字段必填
    backup: <ASBackup>   高级回源的回源addr是否为备源地址，sourceType为advanced时advancedSources字段必填
},
{
    addr: <ASAddr>,
    weight: <ASWeight>,
    backup: <ASBackup>
}
...
]
"""
data = {
    "sourceQiniuBucket": "test-z0",
    "testURLPath": "qiniu_do_not_delete.gif"
}

# 是否开启去问号缓存，默认为false
testURLPath = "qiniu_do_not_delete.gif"

ret, info = cdn_manager.put_source(name, sourceType, data)

print(ret)
print(info)

"""修改回源鉴权：https://developer.qiniu.com/fusion/api/4246/the-domain-name#16"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key, secret_key)

cdn_manager = DomainManager(auth)

# 域名
name = ""

# 是否为七牛私有bucket鉴权，如果是七牛私有bucket，只需要打开 enable开关，本功能将随着回源鉴权功能使能
isQiniuPrivate = True

# 回源鉴权开关
enable = True

"""
注意：如果是 七牛私有bucket鉴权，以下参数不需要填
path: [<Path>, ...],                    要匹配这个回源鉴权的path，目前该功能还不支持
method: <Method>,                       回源鉴权支持的http方法，GET/POST/HEAD
parameters: [<Parameter>, ...],         回源鉴权中参与鉴权的url 参数，取值取决于用户鉴权服务器的鉴权规则
timeLimit: <TimeLimit>,                 回源鉴权的鉴权超时时间，单位ms, 最小 100ms(0.1s), 最大10000ms(10s)
userAuthUrl: <UserAuthUrl>,             回源鉴权: 用户鉴权的鉴权服务地址
strict: <Strict>,                       回源鉴权: 超时后，是否严格为鉴权失败
successStatusCode: <SuccessStatusCode>, 回源鉴权: 鉴权通过的http code, 最小100，最大10000
failureStatusCode: <FailureStatusCode>  回源鉴权: 鉴权失败的http code, 最小100，最大10000
"""
data = {
    "path": ["<Path>", ...],
    "method": "<Method>",
    "parameters": ["<Parameter>", ...],
    "timeLimit": "<TimeLimit>",
    "userAuthUrl": "<UserAuthUrl>",
    "strict": "<Strict>",
    "enable": "<Enable>",
    "successStatusCode": "<SuccessStatusCode>",
    "failureStatusCode": "<FailureStatusCode>"
}

ret, info = cdn_manager.put_bsauth(name, isQiniuPrivate, enable)

print(ret)
print(info)

"""修改特殊配置：https://developer.qiniu.com/fusion/api/4246/the-domain-name#17"""

# 账户ak，sk
access_key = "<access_key>"
secret_key = "<secret_key>"

auth = qiniu.Auth(access_key, secret_key)

cdn_manager = DomainManager(auth)

# 域名
name = "zhuchangzhao2.peterpy.cn"

# bool类型，是否自动开启七牛fop图片处理（备注：不支持平台是动态加速）
enableFop = False

data = {
    # bool类型，是否自动开启图片瘦身（备注：不支持平台是动态加速）
    "enableImageSlim": False,
    # 图片瘦身匹配的指定目录, 例如/abc
    "prefixImageSlims": "[ < PrefixImageSlim >, ...]",
    # 图片瘦身匹配的指定的正则表达式, 例如.*png
    "regexpImageSlims": "[ < RegexpImageSlim >, ...]"
}

ret, info = cdn_manager.put_external(name)

print(ret)
print(info)
