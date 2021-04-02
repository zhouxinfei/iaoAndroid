# !/usr/bin/python
# -*- coding: utf-8 -*-
# 辣妈帮 app version 7.8.00

import time
import requests
import hashlib
import warnings

warnings.filterwarnings("ignore")


def get_params_format(data):
    new_str = "".join(["{}={}&".format(k, v) for k, v in data.items()])
    return new_str[:-1]


def get_md5_encrypt(data):
    return hashlib.md5(data.encode("utf-8")).hexdigest()


def get_sign(params):
    params_format = get_params_format(params)
    params_encrypt = get_md5_encrypt(params_format)
    second_join = params_encrypt + "&key=bec58193ad7a9f2bc143acdb060ecec6"
    sign = get_md5_encrypt(second_join)
    return sign

if __name__ == '__main__':
    params = {
        'v': '4',
        'vendor': 'Pixel',
        'osver': '8.1.0',
        'client_flag': 'lmbang',
        'client_ver': '7.8.00',
        'versioncode': '360',
        'imei': '',
        'device_id': '',
        'channel': 'a360',
        'os': 'android',
        'os_type': 'android',
        'network_type': 'wifi',
        'op_company': '',
        'respond_type': '1080x1794',
        'IDFV': '',
        'IDFA': '',
        'android_id': '14b8312afe35bec6',
        'android_id_token': 'ffffffff-ec38-7ce6-ffff-ffff9a2b52dd',
        'timestamp': '1617358606',
        # 'sign': '5461307497e92add9920d8117033752b',
    }
    print(get_sign(params))
