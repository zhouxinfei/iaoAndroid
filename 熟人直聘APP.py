#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hashlib
import requests
import warnings

warnings.filterwarnings("ignore")


def get_sign(new_s):
    result = hashlib.md5(new_s.encode("utf-8")).hexdigest()
    return result


def send_code(mobile):
    url = "https://srzp-api.shurenzhipin.com/1.0/common/authcode/send"

    headers = {
        # 'Authorization': '',
        # 'register-id': '190e35f7e097ebefaf9',
        # 'device-id': 'FA7220300550',
        # 'device-imei': '',
        # 'device-mac': '',
        # 'device-Oaid': '',
        # 'device-android-id': '7efcabac304449c7',
        # 'client-type': 'app',
        # 'city-name': '',
        # 'city-id': '',
        # 'sub-business-type': 'c',
        # 'Connection': 'close',
        # 'app-platform': 'Android',
        # 'app-version': '8.0.40',
        # 'channel-no': 'oppo',
        # 'latitude': '',
        # 'longitude': '',
        # 'User-Agent': 'Android/com.xinrenlei.koubeigongzuo/8.0.40/20210618/google/AOSPonmsm8996/7.1.2/1080*1920/NETWORK_WIFI/',
        # 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        # 'Content-Length': '71',
        # 'Host': 'srzp-api.shurenzhipin.com',
        # 'Accept-Encoding': 'gzip',
    }
    first_str = f"mobile{str(mobile)}type1"
    first_sign = get_sign(first_str)
    second_str = first_sign + "10CsFgw8DOw7"
    second_sign = get_sign(second_str).upper()
    print("second_sign : ", second_sign)
    data = {
        'type': '1',
        'mobile': mobile,
        # 'request_sign': second_sign,
    }
    response = requests.post(url, headers=headers, data=data, verify=False)
    print(response.text)


if __name__ == '__main__':
    mobile = "18866668888"
    send_code(mobile)
