# !/usr/bin/env python
# -*- coding:utf-8 -*-

import gzip
import json
import time
import hashlib
import requests
from Crypto.Cipher import AES
from Crypto.Util import Padding
from base64 import b64encode
import warnings

warnings.filterwarnings("ignore")


def encode(input):
    key = "6cec4a8b268b8749dfa0bd409effcd08"
    data = gzip.compress(input.encode())
    data = Padding.pad(data, AES.block_size, 'pkcs7')
    aes = AES.new(bytes.fromhex(key), AES.MODE_ECB)
    return b64encode(aes.encrypt(data)).decode('utf-8')


def decode(content):
    key = "6cec4a8b268b8749dfa0bd409effcd08"
    aes = AES.new(bytes.fromhex(key), AES.MODE_ECB)
    data = Padding.unpad(aes.decrypt(content), AES.block_size, 'pkcs7')
    print(data.decode())


def getSign(data):
    salt = "2a7d5d1d3c0a4df08bfbacd58fb0748d"
    ori = ""
    for i in sorted(data):
        ori += i + "=" + data[i] + "&"
    ori += salt
    md5 = hashlib.md5()
    md5.update(ori.encode())
    sign_ = md5.hexdigest().upper()

    md5 = hashlib.md5()
    md5.update((sign_ + salt).encode())
    sign = md5.hexdigest().upper()
    return sign


# 关键词搜索
def getSkuList(city, keyword, page):
    """
    :param city: 地区筛选
    :param keyword: 关键词
    :param page: 翻页
    :return:
    """
    headers = {
        'Host': 'thor.weidian.com',
        'x-schema': 'https',
        'referrer': 'https://android.weidian.com',
        'origin': 'android.weidian.com',
        'x-origin': 'thor',
        'x-encrypt': '1',
        'user-agent': 'Android/8.1.0 WDAPP(WDBuyer/5.7.0) Thor/2.1.3',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    params = "{\"area\":\"\",\"brands\":[],\"chosePoints\":\"\",\"chosePrices\":\"\",\"city\":\"" + city + "\",\"coreWord\":\"\",\"footprintId\":\"5c30df6b68a1e62a097a6b793dd9cd27_1617017322405\",\"id\":\"" + keyword + "\",\"increServices\":[],\"keyword\":\"" + keyword + "\",\"limit\":16,\"page\":" + page + ",\"source\":\"1\",\"tab\":\"all\",\"tags\":[],\"wdServices\":[]}"
    params_encode = encode(params)
    context = "{\"alt\":\"0.0\",\"android_id\":\"2b2081ba28d67929\",\"app_status\":\"active\",\"appid\":\"com.koudai.weidian.buyer\",\"appv\":\"5.7.0\",\"brand\":\"google\",\"build\":\"20190821162153\",\"channel\":\"1013n\",\"cuid\":\"5c30df6b68a1e62a097a6b793dd9cd21\",\"disk_capacity\":\"19.40GB/25.01GB\",\"feature\":\"E|F,H|F,P|F,R|T\",\"h\":\"2392\",\"iccid\":\"89860320045744719592\",\"imei\":\"86798102045247\",\"imsi\":\"460115169646890\",\"is_login\":\"0\",\"lat\":\"29.887301\",\"lon\":\"121.63812\",\"mac\":\"AC:CF:85:B7:39:B9\",\"machine_model\":\"armv8l\",\"memory\":\"1095M/2799M\",\"mid\":\"Nexus_6P\",\"mobile_station\":\"0\",\"net_subtype\":\"0_\",\"network\":\"WIFI\",\"os\":\"27\",\"platform\":\"android\",\"serial_num\":\"ENU7N15A19011383\",\"suid\":\"5c30df6b68a1e62a097a6b793dd9cd29\",\"w\":\"1440\",\"wmac\":\"80:ea:07:96:22:e2\",\"wssid\":\"\\\"阿里巴巴\\\"\"}"
    context_encode = encode(context)

    data = {
        "param": params_encode,
        "v": "2.0",
        "context": context_encode,
        "appkey": "06475281",
        "timestamp": str(int(time.time() * 1000)),
    }

    sign = getSign(data)
    data['sign'] = sign

    response = requests.post('https://thor.weidian.com/faith/search.item/1.7', headers=headers, data=data)
    print(response.text)
    decode(response.content)


# 商品详情
def getDetail(itemid):
    """
    :param itemid: 商品 id
    :return:
    """
    url = "https://thor.weidian.com/detailmjb/getItemInfo/1.1"
    params = {"adsk": "", "itemId": "%s" % itemid}
    params = json.dumps(params, ensure_ascii=False).replace(" ", "")
    params_encode = encode(params)
    context = {"alt": "0.0", "android_id": "2b2085ba28d67921", "app_status": "active",
               "appid": "com.koudai.weidian.buyer", "appv": "5.7.0", "brand": "google", "build": "20190821162151",
               "channel": "1013n", "cuid": "5c30df6b68a1e62a097a6b793dd9cd21", "disk_capacity": "19.35GB/25.01GB",
               "feature": "E|F,H|F,P|F,R|T", "h": "2392", "iccid": "89860320045744719511", "imei": "86798102045241",
               "imsi": "460115169646891", "is_login": "0", "lat": "29.887301", "lon": "121.63812",
               "mac": "AC:CF:85:B7:39:B2", "machine_model": "armv8l", "memory": "940M/2799M", "mid": "Nexus_6P",
               "mobile_station": "0", "net_subtype": "0_", "network": "WIFI", "os": "27", "platform": "android",
               "serial_num": "ENU7N15A19011383", "suid": "5c30df6b68a1e62a097a6b793dd9cd21", "w": "1440",
               "wmac": "80:ea:07:96:21:ea", "wssid": "\"阿里巴巴\""}
    context = json.dumps(context, ensure_ascii=False).replace(" ", "")
    context_encode = encode(context)

    data = {
        "param": params_encode,
        "v": "2.0",
        "context": context_encode,
        "appkey": "06475281",
        "timestamp": str(int(time.time() * 1000)),
    }

    sign = getSign(data)
    data['sign'] = sign

    headers = {
        # "content-length": "931",
        "x-schema": "https",
        "referrer": "https://android.weidian.com",
        "origin": "android.weidian.com",
        "x-origin": "thor",
        "x-encrypt": "1",
        # "accept-encoding": "GLZip",
        "user-agent": "Android/8.1.0 WDAPP(WDBuyer/5.7.0) Thor/2.1.3",
        "content-type": "application/x-www-form-urlencoded; charset=utf-8",
    }

    response = requests.post(url=url, headers=headers, data=data)
    print(response.text)
    decode(response.content)


# 店铺信息
def getShopInfo(userid):
    cookies = {
    }

    headers = {
        'Host': 'weidian.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Nexus 6P Build/OPM7.181205.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 TBS/045520 Mobile Safari/537.36 WDAPP(WDBuyer/5.7.0) appid/com.koudai.weidian.buyer KDJSBridge2/1.1.0',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'x-referer': 'https://android.weidian.com/',
        'x-requested-with': 'com.koudai.weidian.buyer',
        'sec-fetch-site': 'none',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    params = (
        ('userid', userid),
        ('hidTop', '1'),
        ('disableHeaderRefresh', '1'),
        ('wfr', 'item'),
    )

    response = requests.get('https://weidian.com/certDetails.html', headers=headers, params=params, cookies=cookies)
    response.encoding = "utf-8"
    print(response.text)


# 店铺所有商品
def getShopSku(shopId, page):
    headers = {
        'authority': 'thor.weidian.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'origin': 'https://shop843683.v.weidian.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://shop843683.v.weidian.com/',
        'accept-language': 'zh,zh-CN;q=0.9',
    }

    params = (
        ('param', '{"shopId":"%s","page":%s,"limit":20,"tabId":0,"sortOrder":"desc","isFromH5":true}' % (shopId, page)),
    )

    response = requests.get('https://thor.weidian.com/ares/shop.getItemsInShop/1.0', headers=headers, params=params)
    print(response.text)


if __name__ == '__main__':
    # getSkuList("丽水","杨梅","3")
    getDetail(3962774427)
    # getShopInfo(843683)
    # getShopSku(843683, 5)
