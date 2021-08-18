# !/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import requests
import hashlib
import json
import time
import frida

import warnings

warnings.filterwarnings("ignore")

jsCode = """

function hookTest(data){
    var result;
    Java.perform(function(){
        //console.log('Hook Start ！');

        var NetCrypto = Java.use('com.izuiyou.network.NetCrypto');
        var string = Java.use('java.lang.String');
        var url = "https://api.izuiyou.com/account/login";
        var genSign = NetCrypto.generateSign(url, string.$new(data).getBytes());
        console.log("sign : ", genSign);
        result = genSign;

        //console.log('Success！');

    });
    return result;
}
rpc.exports = {
    zuiyou: hookTest
};

"""
os.system("adb forward tcp:27042 tcp:27042")
def get_zuiyou_sign():
    # 调用frida脚本
    process = frida.get_remote_device().attach("cn.xiaochuankeji.tieba")
    script = process.create_script(jsCode)
    # print('[*] Running zuiyou')
    script.load()
    return script.exports

zuiyou_hook = get_zuiyou_sign()

def get_zuiyou_md5(data):
    return hashlib.md5(data.encode("utf-8")).hexdigest()[0:16]

def zuiyou_app_login(phone, password):
    url = "https://api.izuiyou.com/account/login"

    headers = {
        'Request-Type': 'text/json',
        'ZYP': 'mid=238974211',
        'User-Agent': 'okhttp/3.11.0 Zuiyou/4.8.1',
        'Host': 'api.izuiyou.com',
        'Content-Type': 'application/json; charset=utf-8',
        'Content-Length': '337',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Accept': None
    }
    pw = get_zuiyou_md5(password)
    data = {
        "phone": phone,
        "pw": pw,
        "region_code": 86,
        "h_av": "4.8.1",
        "h_dt": 0,
        "h_os": 27,
        "h_app": "zuiyou",
        "h_model": "Pixel",
        "h_did": "725622b411a3e004",
        "h_nt": 1,
        "h_m": 238974211,
        "h_ch": "GDT-jx-20",
        "h_ts": int(time.time() * 1000),
        "token": "TbK3NXDnqMG0MUx0T_pASu5gCtqsaUV4XjVAc8T2PQdP0Cq-0aVYgaGhKK_TThV9yIkci",
        # "token": "T5K9NZFNDjYso_hcTlz1IG68l2lRGcPKOoMj4YSRU1zTwpUOESy4rsVPaGxeALCbovuyj",
        "android_id": "725622b411a3e004"
    }
    # data = '{"phone":"***********","pw":"e10adc3949ba59ab","region_code":86,"h_av":"4.8.1","h_dt":0,"h_os":27,"h_app":"zuiyou","h_model":"Pixel","h_did":"725622b411a3e004","h_nt":1,"h_m":238974211,"h_ch":"GDT-jx-20","h_ts":1601457410607,"token":"T7K3NXDnqMG0MUx0T_pASu5gCtt8HtZJ_CFQ7FzOaBJ3f-e5unHNij3Z7nWE3xvnfZXhw","android_id":"725622b411a3e004"}'
    data_no = json.dumps(data, separators=(',', ':'))
    # print(data_no)
    sign = zuiyou_hook.zuiyou(data_no)
    params = {
        'sign': sign,
    }

    response = requests.post(url, headers=headers, params=params, data=data_no, verify=False)
    print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))


if __name__ == '__main__':
    zuiyou_app_login("***********", "123456")





