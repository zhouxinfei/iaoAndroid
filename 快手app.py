# !/usr/bin/env python
# -*- coding:utf-8 -*-
# 快手 com.smile.gifmaker 6.0.0.7751


import hashlib
import warnings

warnings.filterwarnings("ignore")


def get_new_str(params, data):
    res = {**params, **data}
    data_sorted = sorted(res.items(), key=lambda d: d[0])
    new_s = ''.join(['{}={}'.format(k, v) for k, v in data_sorted])
    return new_s

# __NStokensig
def sha256hex(data):
    data = data + "0eb432aa1c893fc333678aba224a7473"
    sha256 = hashlib.sha256()
    sha256.update(data.encode())
    res = sha256.hexdigest()
    # print("sha256加密结果:", res)
    return res

# sig
def get_sign(data):
    data = data + "382700b563f4"
    sign = hashlib.md5(data.encode("utf-8")).hexdigest()
    # print("md5加密结果:", sign)
    return sign


if __name__ == '__main__':
    data = "cbb76c5d324e627a016d87ce85b68d82"
    print(sha256hex(data))
