# !/usr/bin/env python
# -*- coding:utf-8 -*-


import base64
from Crypto.Cipher import AES
import requests
import datetime
import warnings

warnings.filterwarnings("ignore")


def get_user_data_encrypt(data):
    # 补足字符串长度为16的倍数
    def add_to_16(s):
        while len(s) % 16 != 0:
            s += (16 - len(s) % 16) * chr(16 - len(s) % 16)
        return str.encode(s)  # 返回bytes

    key = 'neteasenewsboard'  # 密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
    # data = '{"userid":"276238855","ursid":""}'  # 待加密文本
    aes = AES.new(str.encode(key), AES.MODE_ECB)  # 初始化加密器，本例采用ECB加密模式
    encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(data))), encoding='utf8').replace('\n', '')  # 加密
    print('pkcs5加密值:', encrypted_text)
    return encrypted_text


def get_user_info():
    url = "https://gw.m.163.com/commons-user-main/api/v1/commons/user/profile/home"

    headers = {
        'Host': 'gw.m.163.com',
        'Connection': 'keep-alive',
        'Content-Length': '64',
        'data4-Sent-Millis': '1603779232233',
        'Add-To-Queue-Millis': '1603779232232',
        'User-Agent': 'NewsApp/72.2 Android/7.1.2 (HUAWEI/VOG-AL00)',
        # 'X-NR-Trace-Id': '1603779232235_112270175_CQkyZjc4ZGI3ODA2OWQ4NjVjCTUyNTQxMTQ3',
        'X-XR-Original-Host': 'gw.m.163.com',
        # 'User-D': 'jjIhfgBQw3db8ujVyVmV+Vvnx/7tNu4StP43xrkXjRYbqxh1FpT705CyJjviF+NZ',
        # 'User-RC': '13tvLBomKmtYAvv3Vfk0Zg==',
        # 'User-L': 'BPrAR0JY0NwtnGwNPUOytChZCnbJEdygwJCOiX3jWoiof4EdzufByxyEf5hdI/Xe2SwH0C/RXsNcwgXw9oys8w==',
        # 'User-LC': 'lcoUkCm/9ivrOR9FC4J5mA==',
        # 'User-N': '7UoAC6yCMflxD4nNLvNU4jz2/HKlcOJy1VgaLKNX7Kd2cZyvwVzCSrqGz+okse9G',
        # 'User-C': '5rG96L2m',
        # 'User-OD': 'jjIhfgBQw3db8ujVyVmV+Vvnx/7tNu4StP43xrkXjRYbqxh1FpT705CyJjviF+NZ',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    data_before = '{"userid":"276238855","ursid":""}'  # nick":"乔布斯2002"
    # data_before = '{"userid":"272803090","ursid":""}'  # nick":"我是煎饼侠"
    data_after = get_user_data_encrypt(data_before)
    # data_after = "Yuz87vf0h6MoUhuPJqbm9jtKw4ttAPa5x1BMXDDnAwBsv184ELN6RkcBbPvT86/v"

    response = requests.post(url, headers=headers, data=data_after, verify=False)
    print(response.text)


if __name__ == '__main__':
    # data = '31.22240345540261#121.48126708183688#1603792341225#310000'
    # data = '{"userid":"276238855","ursid":""}'
    # get_user_data_encrypt(data)

    get_user_info()
