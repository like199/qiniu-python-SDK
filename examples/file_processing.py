# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, PersistentFop, urlsafe_base64_encode

"""大量文件压缩mode=4：https://developer.qiniu.com/dora/api/1667/mkzip#2"""

access_key = "<access_key>"
secret_key = "<secret_key>"
q = Auth(access_key, secret_key)

# 要压缩的文件所在的空间和索引文件名。
bucket = "upload16"
# 包含压缩信息的txt文件
# 文件内容信息示例
# def create_upload():
#     url1 = urlsafe_base64_encode("http://q28a85rsu.bkt.clouddn.com/484j1s4yuzcapl.jpg")
#     url2 = urlsafe_base64_encode("http://q28a85rsu.bkt.clouddn.com/1575858421000014.png")
#     url3 = urlsafe_base64_encode("http://q28a85rsu.bkt.clouddn.com/001575858514000877.jpeg")
#     url4 = urlsafe_base64_encode("http://q28a85rsu.bkt.clouddn.com/001575858421000014.png")
#     f = open("./test1.txt", "a")
#     f.write(url1)
#     f.write(url2)
#     f.write(url3)
#     f.write(url4)
key = "test1.txt"

# 压缩是使用的队列名称。
pipeline = "test_01"

# 压缩规格
mkzipArgs = "mkzip/4"

# 可以对压缩后的文件进行使用saveas参数自定义命名，当然也可以不指定文件会默认命名并保存在当前空间
saveas_key = urlsafe_base64_encode("upload17:test25.zip")
fops = mkzipArgs + "|saveas/" + saveas_key

pfop = PersistentFop(q, bucket, pipeline)
ops = []
ops.append(fops)
ret, info = pfop.execute(key, ops, 1)
print(info)
assert ret['persistentId'] is not None

"""少量文件压缩mode=2：https://developer.qiniu.com/dora/api/1667/mkzip#1"""

access_key = "<access_key>"
secret_key = "<secret_key>"

q = Auth(access_key, secret_key)

# 要压缩文件所在空间
bucket = "upload26"

# 文件名
key = "00Fi2jmptt419K3vKP-LOhvzOmj_WZ"

# 压缩是使用的队列名称。
pipeline = "test_01"

url = urlsafe_base64_encode("http://q7l1lwj1m.bkt.clouddn.com/00Fi2jmptt419K3vKP-LOhvzOmj_WZ")

# 压缩规格
mkzipArgs = "mkzip/2/encoding/utf-8/url/{0}".format(url)

# 可以对压缩后的文件进行使用saveas参数自定义命名，当然也可以不指定文件会默认命名并保存在当前空间
saveas_key = urlsafe_base64_encode("upload26:mode2.zip")
fops = mkzipArgs + "|saveas/" + saveas_key

pfop = PersistentFop(q, bucket, pipeline)
ops = []
ops.append(fops)
ret, info = pfop.execute(key, ops, 1)
print(info)
assert ret['persistentId'] is not None

"""文本文件合并：https://developer.qiniu.com/dora/api/1253/text-file-merging-concat"""

access_key = "<access_key>"
secret_key = "<secret_key>"
q = Auth(access_key, secret_key)

# 要压缩文件所在空间
bucket = "upload26"

# 合并的源文本文件
key = "0.txt"

# 压缩是使用的队列名称。
pipeline = 'test_01'

# 需要合并合并的文本文件1
url1 = urlsafe_base64_encode("http://q7l1lwj1m.bkt.clouddn.com/1.txt")

# 需要合并合并的文本文件2
url2 = urlsafe_base64_encode("http://q7l1lwj1m.bkt.clouddn.com/2.txt")

# 文件类型
mimeType = urlsafe_base64_encode("text/plain")

# 压缩规格
mkzipArgs = "concat/mimeType/{0}/{1}/{2}".format(mimeType, url1, url2)

# 可以对压缩后的文件进行使用saveas参数自定义命名，当然也可以不指定文件会默认命名并保存在当前空间
saveas_key = urlsafe_base64_encode('upload26')
fops = mkzipArgs + '|saveas/' + saveas_key

pfop = PersistentFop(q, bucket, pipeline)
ops = []
ops.append(fops)
ret, info = pfop.execute(key, ops, 1)
print(info)
assert ret['persistentId'] is not None
