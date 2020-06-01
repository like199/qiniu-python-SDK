# # -*- coding: utf-8 -*-
# # flake8: noqa
# flake8: noqa
from qiniu import Auth, PersistentFop

"""阿里音频审核服务：https://developer.qiniu.com/dora/api/6392/ali-audio-audit-service"""

access_key = "<access_key>"
secret_key = "<secret_key>"

q = Auth(access_key, secret_key)

# 要压缩文件所在空间
bucket = "upload26"

# 合并的源文本文件
key = "20200327111522.mp3"

# 队列名称。
pipeline = 'test_01'

# fops名称：ali_audio
fops = "ali_audio"

pfop = PersistentFop(q, bucket, pipeline)
ops = []
ops.append(fops)
ret, info = pfop.execute(key, ops, 1)
print(info)
assert ret['persistentId'] is not None
