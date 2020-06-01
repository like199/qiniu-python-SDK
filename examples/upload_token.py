# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth

# 需要填写你的 Access Key 和 Secret Key
# access_key = ''
# secret_key = ''
access_key = 'wxCLv4yl_5saIuOHbbZbkP-Ef3kFFFeCDYmwTdg3'
secret_key = 'cxqR6aaTGlTzuSCe2V5Zea8oaQID9CC5iRTEqI6t'

# 构建鉴权对象
q = Auth(access_key, secret_key)

# 要上传的空间
bucket_name = 'upload28'

# 上传到七牛后保存的文件名
key = 'ceshi'

# 生成上传 Token，可以指定过期时间等

# 上传策略示例
# https://developer.qiniu.com/kodo/manual/1206/put-policy
policy = {
    # 'callbackUrl':'https://requestb.in/1c7q2d31',
    # 'callbackBody':'filename=$(fname)&filesize=$(fsize)'
    # 'persistentOps':'imageView2/1/w/200/h/200'
}

token = q.upload_token(bucket_name, key, 3600, policy)

print(token)
