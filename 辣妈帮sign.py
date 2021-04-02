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


# def get_cookies():
#     url = "https://open.lmbang.com/user-guest/index"
#     headers = {
#         'Accept-Language': 'zh-CN,zh;q=0.8',
#         'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; Pixel Build/OPM1.171019.011) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
#         'Connection': 'close',
#         'Host': 'open.lmbang.com',
#         'Accept-Encoding': 'gzip',
#     }
#     params = {
#         'v': '4',
#         'vendor': 'Pixel',
#         'osver': '8.1.0',
#         'client_flag': 'lmbang',
#         'client_ver': '7.8.00',
#         'versioncode': '360',
#         'imei': '',
#         'device_id': '',
#         'channel': 'a360',
#         'os': 'android',
#         'os_type': 'android',
#         'network_type': 'wifi',
#         'op_company': '',
#         'respond_type': '1080x1794',
#         'IDFV': '',
#         'IDFA': '',
#         'android_id': '14b8312afe35bec6',
#         'android_id_token': 'ffffffff-ec38-7ce6-ffff-ffff9a2b52dd',
#         'timestamp': str(int(time.time())),
#         # 'timestamp': '1617358606',
#         # 'sign': '5461307497e92add9920d8117033752b',
#     }
#     sign = get_sign(params)
#     params["sign"] = sign
#     response = requests.get(url, headers=headers, params=params, verify=False)
#     print(response.json())
#     print(response.cookies)
#     return response.cookies
#
#
# def get_content(cookies):
#     url = "https://open.lmbang.com/topic/interface/content"
#     headers = {
#         'Accept-Language': 'zh-CN,zh;q=0.8',
#         'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; Pixel Build/OPM1.171019.011) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
#         'Connection': 'close',
#         # 'Cookie': 't_skey=224e30734dbea18e851ac967711fed74; LMB_AUTH_CODE=224e30734dbea18e851ac967711fed74; __TOKEN_NEW=SESS_2f469wG8Fv2et3FP2IhdGNTc9RW6DKJlibO4gW1eUhV3j4jkhvgv6HQQXwoqk32pYzl3uC90M9t1zyTm5K4Vtyd%2FP6H8G4vrtFAzvCONaJNqb4WH2mzURrKQ',
#         'Host': 'open.lmbang.com',
#         'Accept-Encoding': 'gzip',
#     }
#     params = {
#         'v': '4',
#         'source_from': '1_2',
#         'tid': '57725985',
#         'vendor': 'Pixel',
#         'osver': '8.1.0',
#         'client_flag': 'lmbang',
#         'client_ver': '7.8.00',
#         'versioncode': '360',
#         'imei': '',
#         'device_id': '',
#         'channel': 'a360',
#         'os': 'android',
#         'os_type': 'android',
#         'network_type': 'wifi',
#         'op_company': '',
#         'respond_type': '1080x1794',
#         'IDFV': '',
#         'IDFA': '',
#         'android_id': '14b8312afe35bec6',
#         'android_id_token': 'ffffffff-ec38-7ce6-ffff-ffff9a2b52dd',
#         'timestamp': str(int(time.time())),
#         # 'timestamp': '1617357173',
#         # 'sign': 'cbca90a4d1aafa3b8279a4ef161e4345',
#     }
#     sign = get_sign(params)
#     params["sign"] = sign
#     response = requests.get(url, headers=headers, params=params, cookies=cookies, verify=False)
#     print(response.json())
#
#
# if __name__ == '__main__':
#     cookies = get_cookies()
#     get_content(cookies)
