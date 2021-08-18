# !/usr/bin/python
# -*- coding: utf-8 -*-

import base64
import time
from urllib.parse import urlparse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import warnings

warnings.filterwarnings("ignore")


def waimai_sign_v0():
    base_url = 'http://wmapi.meituan.com/api/v7/poi/homepage'
    req_time = int(time.time())
    wm_seq = req_time % 1000
    urlpath = urlparse(base_url).path
    utm_content = ''
    sign_data = f'{urlpath}/{utm_content}/{req_time}/{wm_seq}'
    sign_data = sign_data.encode('utf-8')
    rsa_key = u'''
        -----BEGIN RSA PUBLIC KEY-----
        MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCsFOSlHxuOEalZccpOvX4jFGMfE3WWpmpD+i15
        Ky/YRHy9ZVPVkfAKi51Y6Lozwikxeg0SLJZdhKKGEUqWPDriaUyBZl1a8EyApxy/NQzUxmKA3I+t
        vmuO2nsuw9DFDhUIUERe+E06QZJmKsE12RLCyixoF2157GTKz/NAiUgraQIDAQAB
        -----END RSA PUBLIC KEY-----
        '''
    rsa_key = rsa_key.strip()
    rsa_key = RSA.importKey(rsa_key)
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    sign_result = base64.b64encode(cipher.encrypt(sign_data)).decode('utf-8')
    return sign_result


if __name__ == '__main__':
    print(waimai_sign_v0())
