import os
import uuid
import datetime
import requests
import json
#修改文件名


def change_filename(filename):
    fileinfo = os.path.splitext(filename)
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+str(uuid.uuid4().hex)+fileinfo[-1]
    return filename

#模拟post/get请求
def curl(url, params, type):
    baseUrl = 'https://tsapi.amap.com/v1/track/'
    url = baseUrl + url
    params["sid"] = 118476
    params["key"] = '01b6e8c78f8f2d7ee079d0a51c88ba50'
    if type == 'GET':
        response = requests.get(url, params)
    else:
        response = requests.post(url, params)
    res = json.loads(response.content)
    print(res)
    return res