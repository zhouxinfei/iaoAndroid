# !/usr/bin/env python
# -*- coding:utf-8 -*-
# https://www.poi86.com/

import time
import json
import requests
from urllib import parse
import warnings

warnings.filterwarnings("ignore")

url = "https://api2.xingse.net/v3_10/item/get_nearby_items"

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '271',
    'Host': 'api2.xingse.net',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.5.0',
    'Accept': None
}

data = {
    '__user_id': '52866661',
    'distance': '27.342319608694403',
    '__access_token': '6726358796098e74d778666.83344592',
    'latitude': '22.522054',
    'scale_level': '4',
    '__version': '3.14.5',
    '__device_region': '0',
    '__device_type': '0',
    'page': '0',
    '__device_id': '3b084d96-bcb3-33b0-897d-99408680b123',
    'longitude': '114.079118',
}

response = requests.post(url, headers=headers, data=data, verify=False)
print(json.dumps(json.loads(response.text), ensure_ascii=False))

# distance

# package com.test;
#
# public class demo01 {
#     public static void main(String[] args) {
#
# //        double lat1 = 22.29100699605476;
# //        double long1 = 114.1771202129474;
# //        double lat2 = 22.282354622954898;
# //        double long2 = 114.1739421999315;
#
#         double lat1 = 22.287900;
#         double long1 = 114.160870;
#         double lat2 = 22.522054;
#         double long2 = 114.079118;
#
#         double distance = calculateHaversineMI(lat1, long1, lat2, long2);
#         System.out.println(distance);
#     }
#
#     public static double calculateHaversineMI(double lat1, double long1, double lat2,double long2) {
#         double dlong = (long2 - long1) * (Math.PI / 180.0f);
#         double dlat = (lat2 - lat1) * (Math.PI / 180.0f);
#         double a = Math.pow(Math.sin(dlat / 2.0), 2)
#                 + Math.cos(lat1 * (Math.PI / 180.0f))
#                 * Math.cos(lat2 * (Math.PI / 180.0f))
#                 * Math.pow(Math.sin(dlong / 2.0), 2);
#         double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
#         double d = 6367* c;
#         return d;
#     }
# }
