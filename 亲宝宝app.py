# !/usr/bin/env python
# -*- coding:utf-8 -*-


import json
import requests
import time
import base64
import hashlib
import hmac
from hashlib import sha1
from pyDes import *  # pip install pyDes
import warnings

warnings.filterwarnings("ignore")

def get_sign(params_dict):
    salt = 'cgva5ezuh5'
    # salt = 'caf12ca905'
    params_string = get_sort_string(params_dict)
    salt_string = '{}{}{}'.format(salt, params_string, salt)
    # print(salt_string)
    sign = hash_hmac(salt_string, salt, sha1)
    return sign

def get_sort_string(params_dict):
    params_list = []
    a = sorted(params_dict.items(), key=lambda x: x[1], reverse=False)
    for aa in a:
        params_list.append(aa[1])
    params_string = ''.join(params_list)
    return params_string

def hash_hmac(code, key, sha1):
    hmac_code = hmac.new(key.encode(), code.encode(), sha1).digest()
    return base64.b64encode(hmac_code).decode().replace("+", ".").replace("/", "_")

def get_bodySign_md5(data):
    m = hashlib.md5(data.encode("utf-8"))
    return m.hexdigest()

class DEncry:
    def __init__(self, Des_Key):
        self.Des_Key = Des_Key  # Key
        self.Des_IV = ""  # 自定IV向量

    # 使用DES加base64的形式加密
    def encrypt(self, s):
        k = des(self.Des_Key, CBC, self.Des_IV, pad=None, padmode=PAD_PKCS5)
        EncryptStr = k.encrypt(s)
        # EncryptStr = binascii.unhexlify(k.encrypt(str))
        return base64.b64encode(EncryptStr).decode().replace("+", ".").replace("/", "_")  # 转base64编码返回



def qinbaobao_login(token):
    url = "https://apiuser.qbb6.com/user/login"
    headers = {
        "User-Agent": None,
        "Accept-Encoding": "gzip",
        "Accept": "application/json",
        "Content-type": "application/json",
        "Content-Length": "536",
        "Host": "apiuser.qbb6.com",
        "Connection": "Keep-Alive",
    }

    """
    模拟登陆 用户名 密码 加密
    加密方法 DES/CBC/PKCS5Padding
    
    token = "6431ca6e-d7c2-4ce6-9e16-806878fb92a3"
    username = ""
    password = ""
    substring = token[0: len(token) // 5]
    substring2 = token[len(token) * 3 // 5: len(token) * 4 // 5]
    加密前:
    un = substring + username + substring2
    pwd = substring + password + substring2
    
    getAppSecret = "cgva5ezuh5"
    DES 密码:
    des_pwd = getAppSecret[0:8]
    
    des 偏移量 : IV ""
    
    byte[] a = {1, 2, 3, 4, 5, 6, 7, 8};
    String IV = new String(a);
    System.out.println(IV);  
    
    """
    username = "用户名"
    password = "密码"
    substring = token[0: len(token) // 5]
    substring2 = token[len(token) * 3 // 5: len(token) * 4 // 5]
    getAppSecret = "cgva5ezuh5"
    des_pwd = getAppSecret[0:8]

    # script = hook_prepare()
    # uns = substring + username + substring2
    # # print("uns : ", uns)
    # account = script.exports.getsig(uns, des_pwd)
    # # print("account : ", account)
    # pwds = substring + password + substring2
    # # print("pwds : ", pwds)
    # pwd = script.exports.getsig(pwds, des_pwd)
    # # print("pwd : ", pwd)

    uns = substring + username + substring2
    pwds = substring + password + substring2

    des_encrypt = DEncry(des_pwd)
    account = des_encrypt.encrypt(uns)
    print("account : ", account)
    pwd = des_encrypt.encrypt(pwds)
    print("pwd : ", pwd)


    data = {
        "account": account,
        # "account": "KYyisNHlUy4Hsf7AxzIA4zU9RPHttk5KgYu.lOvZmYc=",
        "accountType": 0,
        "areaCode": "86",
        "pwd": pwd
        # "pwd": "n5D1fomwK2D0ADA1dkG_u919rr0jjF0V"
    }
    new_data = json.dumps(data, separators=(',', ':'))
    bodySign = get_bodySign_md5(new_data)
    params = {
        "protocol": "1",
        "appKey": "48vt2wum0nev4s68",
        "versionCode": "324",
        "token": token,
        # "token": "7b55fa91-0577-4af8-9d93-d85422f0a24b",
        "bodySign": bodySign,
        # "bodySign": "01d39f9c06a622783f8dcec29736971f",
        "lang": "zh-CN",
        "timestamp": str(int(time.time() * 1000)),
        # "timestamp": "1583823801196",
        "channel": "1012",
        # "sign": "weNK_FyPUZBCc.TIm_w2qcJD8Qo=",
    }
    sign = get_sign(params)
    params["sign"] = sign
    response = requests.post(url, headers=headers, params=params, data=new_data, verify=False)
    print(response.text)

    print("结果 token : ", token)


def get_toekn():
    url = "https://apiuser.qbb6.com/auth"
    headers = {
        "User-Agent": None,
        "Accept-Encoding": "gzip",
        "Accept": "application/json",
        "Content-type": "application/json",
        "Content-Length": "536",
        "Host": "apiuser.qbb6.com",
        "Connection": "Keep-Alive",
        # "Cookie": "acw_tc=76b20ffc15838089162377074e1cee034baf14df0850de07313b318639d43a",
        # "Cookie2": "$Version=1",
    }
    data = {
        "androidId": "f8ee17ea05a6ebac",
        "brand": "Android",
        "channel": 1012,
        "deviceType": 1,
        "dh": 960,
        "dw": 540,
        "imeiCode": "910000000037621",
        "ipHost": "10.0.3.15",
        "model": "MuMu",
        "netOperator": 0,
        "network": 1,
        "orientation": 1,
        "os": "android",
        "pixelRatio": 180,
        "screenHeight": 960,
        "screenWidth": 540,
        "userAgent": "Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36; trackinfo/null versioncode/324 env/prod deviceid/910000000037621 token/null",
        "version": "6.0.1"
    }
    new_data = json.dumps(data, separators=(',', ':'))
    bodySign = get_bodySign_md5(new_data)
    params = {
        "protocol": "1",
        "device": "910000000037621",
        "appKey": "48vt2wum0nev4s68",
        "imeiCode": "910000000037621",
        "versionCode": "324",
        "bodySign": bodySign,
        # "bodySign": "5b8ee06dac8c806c9f2ce3497f87383c",
        "lang": "zh-CN",
        "timestamp": str(int(time.time() * 1000)),
        # "timestamp": "1583816953462",
        "channel": "1012",
        # "sign": "Og0m0tPdbPjX4LU4VIBRMg8IQ7k=",
    }
    sign = get_sign(params)
    params["sign"] = sign
    response = requests.post(url, headers=headers, params=params, data=new_data, verify=False)
    token = json.loads(response.text).get("token")
    print("token : {}".format(token))
    return token


if __name__ == '__main__':
    token = get_toekn()
    qinbaobao_login(token)
