# -*- coding: utf-8 -*-
from qiniu import Auth

access_key = '公钥'
secret_key = '私钥'
url = "http://ai.qiniuapi.com/v1/image/groups/search"

AccessToken = Auth(access_key, secret_key)
print(AccessToken.token_of_request(url))
