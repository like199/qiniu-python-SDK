from qiniu import Auth, http, urlsafe_base64_encode, append_file
import time

# 填写七牛账号的公私钥
access_key = '<access_key>'
secret_key = '<secret_key>'

# 要上传的空间
bucket_name = "upload30"

# 构建鉴权对象
q = Auth(access_key, secret_key)

# 上传后保存的文件名
key = "append_{0}.txt".format(int(time.time()))

# 生成上传token，可以指定过期时间
token = q.upload_token(bucket_name)


def file2base64(localfile):
    with open(localfile, 'rb') as f:  # 以二进制读取文件
        data = f.read()

    return data


#  要上传的文件路径
localfile = "./append.txt"

data = file2base64(localfile)

#  首次追加文件设置为0，后续追加时，值为前一次追加后返回的偏移量
offset = 0

encodekey = urlsafe_base64_encode(key)

ret, info = append_file(token, encodekey, data, offset)
print(ret)
print(info)

