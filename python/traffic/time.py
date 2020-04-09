import json

import time
from threading import Timer


# def carTrack(i=0):
#     print(i)
#     i=i+1
#     t = Timer(2, carTrack)
#     t.start()
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
    #paths = "122.514694,37.16684;122.515549,37.166847;122.515579,37.166882;122.515564,37.16737;122.515564,37.168201;122.515541,37.168812;122.515495,37.168839;122.515099,37.168839"
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
# def carTrack():
#     l = [["116.964624", "36.614668"], ["122.081238", "37.530827"], ["122.081726", "37.530617"],
#          ["122.081337", "37.530037"], ["122.083855", "37.529011"], ["122.083946", "37.529148"],
#          ["122.085365", "37.528564"], ["122.081718", "37.521481"], ["122.09819", "37.514774"],
#          ["122.095543", "37.494003"], ["122.106781", "37.49073"], ["122.130486", "37.456974"],
#          ["122.125992", "37.452332"], ["122.155731", "37.377285"], ["122.155518", "37.374012"],
#          ["122.151291", "37.373714"], ["122.152237", "37.373764"], ["122.203102", "37.355515"],
#          ["122.24752", "37.29871"], ["122.245903", "37.299374"], ["122.284042", "37.313313"],
#          ["122.33873", "37.250328"], ["122.451141", "37.231956"], ["122.458176", "37.2314"], ["122.460892", "37.18116"],
#          ["122.518028", "37.182842"], ["122.519974", "37.17477"], ["122.511909", "37.169106"],
#          ["122.515038", "37.171474"], ["122.513771", "37.168591"], ["122.51313", "37.168259"],
#          ["122.51342", "37.167046"], ["116.48303839", "39.990633"]]
#     for i in range(0,len(l)-1):
#         str = l[i][0] + ',' + l[i][1]
#         millis = int(round(time.time() * 1000))
#         point = json.dumps([{"location": str, "locatetime": millis}])
#         params = {
#             'tid': 246882981,
#             'trid': 20,
#             'points': point
#         }
#         response = curl('point/upload', params, 'POST')
#         print(response['errcode'],response['errmsg'])
#         time.sleep(2)



if __name__ == "__main__":
    carTrack()

