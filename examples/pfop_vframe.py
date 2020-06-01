# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, PersistentFop, urlsafe_base64_encode

# 对已经上传到七牛的视频发起异步转码操作
# 自己AK/SK
access_key = 'wxCLv4yl_5saIuOHbbZbkP-Ef3kFFFeCDYmwTdg3'
secret_key = 'cxqR6aaTGlTzuSCe2V5Zea8oaQID9CC5iRTEqI6t'
q = Auth(access_key, secret_key)

# 要转码的文件所在的空间和文件名。
bucket = 'upload24'
key = 'zhuanmp4.mp4'

# 转码是使用的队列名称。
pipeline = 'test_01'

# wmimage = urlsafe_base64_encode("http://q600x64lb.sabkt.gdipper.com/logo.png")
# # 要进行视频截图操作。
# fops = "avthumb/mp3/acodec/aac"
fops = 'avthumb/m3u8/segtime/10/noDomain/1/pattern/' + urlsafe_base64_encode("niuchao$(count).ts")

# 可以对转码后的文件进行使用saveas参数自定义命名，当然也可以不指定文件会默认命名并保存在当前空间
saveas_key = urlsafe_base64_encode('upload24:ceshi111.m3u8')
fops = fops + '|saveas/' + saveas_key

pfop = PersistentFop(q, bucket, pipeline)
ops = []
ops.append(fops)
ret, info = pfop.execute(key, ops, 1)
print(info)
assert ret['persistentId'] is not None
