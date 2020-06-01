# -*- coding: utf-8 -*-

from qiniu import config
from qiniu import http
from qiniu.utils import urlsafe_base64_encode, entry


class MkZip(object):
    """多文件压缩

    主要涉及多文件压缩，具体的接口规格可以参考：
    https://developer.qiniu.com/dora/api/1667/mkzip

    Attributes:
        auth: 账号管理密钥对，Auth对象
    """

    def __init__(self, auth):
        self.auth = auth

    def change_status(self, bucket, key, status, cond):
        """修改文件的状态

        修改文件的存储类型为可用或禁用：

        Args:
            bucket:         待操作资源所在空间
            key:            待操作资源文件名
            storage_type:   待操作资源存储类型，0为启用，1为禁用
        """
        resource = entry(bucket, key)
        if cond and isinstance(cond, dict):
            condstr = ""
            for k, v in cond.items():
                condstr += "{0}={1}&".format(k, v)
            condstr = urlsafe_base64_encode(condstr[:-1])
            return self.__rs_do('chstatus', resource, 'status/{0}'.format(status), 'cond', condstr)
        return self.__rs_do('chstatus', resource, 'status/{0}'.format(status))

    def __uc_do(self, operation, *args):
        return self.__server_do(config.get_default('default_uc_host'), operation, *args)

    def __rs_do(self, operation, *args):
        return self.__server_do(config.get_default('default_rs_host'), operation, *args)

    def __io_do(self, bucket, operation, *args):
        ak = self.auth.get_access_key()
        io_host = self.zone.get_io_host(ak, bucket)
        return self.__server_do(io_host, operation, *args)

    def __server_do(self, host, operation, *args):
        cmd = _build_op(operation, *args)
        url = '{0}/{1}'.format(host, cmd)
        return self.__post(url)

    def __post(self, url, data=None):
        return http._post_with_auth(url, data, self.auth)

    def __get(self, url, params=None):
        return http._get(url, params, self.auth)


def _build_op(*args):
    return '/'.join(args)


def build_batch_copy(source_bucket, key_pairs, target_bucket, force='false'):
    return _two_key_batch('copy', source_bucket, key_pairs, target_bucket, force)


def build_batch_rename(bucket, key_pairs, force='false'):
    return build_batch_move(bucket, key_pairs, bucket, force)


def build_batch_move(source_bucket, key_pairs, target_bucket, force='false'):
    return _two_key_batch('move', source_bucket, key_pairs, target_bucket, force)


def build_batch_delete(bucket, keys):
    return _one_key_batch('delete', bucket, keys)


def build_batch_stat(bucket, keys):
    return _one_key_batch('stat', bucket, keys)


def _one_key_batch(operation, bucket, keys):
    return [_build_op(operation, entry(bucket, key)) for key in keys]


def _two_key_batch(operation, source_bucket, key_pairs, target_bucket, force='false'):
    if target_bucket is None:
        target_bucket = source_bucket
    return [_build_op(operation, entry(source_bucket, k), entry(target_bucket, v), 'force/{0}'.format(force)) for k, v
            in key_pairs.items()]
