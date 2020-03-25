import os
import re
import uuid
import datetime
import requests
import json

#模拟post/get请求
def curl(url, params, type):
    baseUrl = 'https://restapi.amap.com/'
    url = baseUrl + url
    params["key"] = '01b6e8c78f8f2d7ee079d0a51c88ba50'
    if type == 'GET':
        response = requests.get(url, params)
    else:
        response = requests.post(url, params)
    res = json.loads(response.text)
    print(res)
    return res

def geocode_curl(address):
    params = {}
    url = 'https://restapi.amap.com/v3/geocode/geo'
    params["address"] = address
    params["key"] = '01b6e8c78f8f2d7ee079d0a51c88ba50'
    response = requests.get(url, params)
    res = json.loads(response.content)
    return res['geocodes'][0]['location']

def driving_curl(params):
    url = 'https://restapi.amap.com/v3/direction/driving'
    params["key"] = '01b6e8c78f8f2d7ee079d0a51c88ba50'
    response = requests.get(url, params)
    res = json.loads(response.content)
    return res

# params = {}
# url = 'v3/direction/driving?origin=116.964624,36.614668&destination=116.483038,39.990633'
# t = curl(url, params, 'GET')
# print(t)
# t = geocode_curl('北京市朝阳区阜通东大街6号')
# print(t)
params = {
    'origin' : '116.964624,36.614668',
    'destination' : '116.483038,39.990633'
}
t = driving_curl(params)
k = t['route']['paths'][0]['steps']
paths = [['116.964624','36.614668']]
for m in k:
    pp = m['polyline'].split(';')[0].split(',')
    print(pp)
    paths.append(pp)
paths.append(['116.48303839','39.990633'])
print(paths)
