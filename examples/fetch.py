# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth
from qiniu import BucketManager

# 自己
# access_key = 'wxCLv4yl_5saIuOHbbZbkP-Ef3kFFFeCDYmwTdg3'
# secret_key = 'cxqR6aaTGlTzuSCe2V5Zea8oaQID9CC5iRTEqI6t'

access_key = 'Lq3kRYbrKxv3XoDzxvD_4tjjvCCz32NKAEBmSjnl'
secret_key = 'uW2T4BcLAlUw9QncsEB5hcgpzedYtbgouFHCtOIA'

bucket_name = 'qss-cdn'

q = Auth(access_key, secret_key)

bucket = BucketManager(q)

url = 'http://devtools.qiniu.com/qiniu.png'

key = 'qiniu.png'

ret, info = bucket.fetch(url, bucket_name, key)
print(info)
assert ret['key'] == key
