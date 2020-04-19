import json

import time
from threading import Timer

from app.lib.functions import curl, driving_curl, geocode_curl


def carTrack():
    origin = geocode_curl('山东省威海市荣成市哈尔滨理工大学荣成校区')
    destination = geocode_curl('山东省威海市哈尔滨工业大学')
    print(origin, destination)
    params = {
        'origin': origin,
        'destination': destination
    }
    paths = [origin.split(',')]
    driving = driving_curl(params)
    steps = driving['route']['paths'][0]['steps']
    print(len(steps))
    paths = ''
    for i in range(len(steps)):
        paths += steps[i]['polyline']
    l = paths.split(';')
    for i in range(len(l)):
        str = l[i]
        millis = int(round(time.time() * 1000))
        point = json.dumps([{"location": str, "locatetime": millis}])
        params = {
            'tid': 246882981,
            'trid': 40,
            'points': point
        }
        response = curl('point/upload', params, 'POST')
        print(response['errcode'],response['errmsg'])
        time.sleep(1)



if __name__ == "__main__":
    carTrack()

