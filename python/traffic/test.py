import calendar
import os
import re
import uuid
import datetime
import requests
import json
import time

#模拟post/get请求
from sqlalchemy import func

from app import db
from app.models import Expense, Schedule, Track

# def curl(url, params, type):
#     baseUrl = 'https://restapi.amap.com/'
#     url = baseUrl + url
#     params["key"] = '01b6e8c78f8f2d7ee079d0a51c88ba50'
#     if type == 'GET':
#         response = requests.get(url, params)
#     else:
#         response = requests.post(url, params)
#     res = json.loads(response.text)
#     print(res)
#     return res
#
# def geocode_curl(address):
#     params = {}
#     url = 'https://restapi.amap.com/v3/geocode/geo'
#     params["address"] = address
#     params["key"] = '01b6e8c78f8f2d7ee079d0a51c88ba50'
#     response = requests.get(url, params)
#     res = json.loads(response.content)
#     print(res)
#     return res['geocodes'][0]['location']
#
#
# def driving_curl(params):
#     url = 'https://restapi.amap.com/v3/direction/driving'
#     params["key"] = '01b6e8c78f8f2d7ee079d0a51c88ba50'
#     response = requests.get(url, params)
#     res = json.loads(response.content)
#     return res
#
# origin = geocode_curl('山东省威海市荣成市哈尔滨理工大学荣成校区')
# destination = geocode_curl('山东省威海市哈尔滨工业大学')
# print(origin,destination)
# params = {
#         'origin': origin,
#         'destination': destination
#     }
# paths = [origin.split(',')]
# driving = driving_curl(params)
# steps = driving['route']['paths'][0]['steps']
# print(len(steps))
# str = ''
# for i in range(len(steps)):
#     str += steps[i]['polyline']
# p = str.split(';')
# print(p)
# paths = "122.514694,37.16684;122.515549,37.166847;122.515579,37.166882;122.515564,37.16737;122.515564,37.168201;122.515541,37.168812;122.515495,37.168839;122.515099,37.168839"
# p = paths.split(';')
# print(p)
# params = {}
# url = 'v3/direction/driving?origin=116.964624,36.614668&destination=116.483038,39.990633'
# t = curl(url, params, 'GET')
# print(t)
# t = geocode_curl('北京市朝阳区阜通东大街6号')
# print(t)
# origin = '116.964624,36.614668'
# destination = '116.483038,39.990633'
# params = {
#     'origin' : origin,
#     'destination' : destination
# }
# t = driving_curl(params)
# k = t['route']['paths'][0]['steps']
# start_point = origin.split(',')
# end_point = destination.split(',')
# paths = [start_point]
# for m in k:
#     pp = m['polyline'].split(';')[0].split(',')
#     paths.append(pp)
# paths.append(end_point)
# data = {}
# data['distance'] = t['route']['paths'][0]['distance']
# data['duration'] = t['route']['paths'][0]['duration']
# data['steps'] = paths
# print(data)



# from dateutil.relativedelta import relativedelta
#
# def LF(year,month):
#     FL = []
#     firstDayWeekDay, monthRange = calendar.monthrange(year, month)
#     firstDay = datetime.date(year=year, month=month, day=1)
#     lastDay = datetime.date(year=year, month=month, day=monthRange)
#     FL.append(firstDay)
#     FL.append(lastDay)
#     return FL
#
# def halfYear():
#     start = datetime.date.today() - relativedelta(months=5)
#     end = datetime.datetime.now()
#     month_num = 12 * (end.year - start.year) + end.month - start.month
#     time_list = []
#     year = start.year
#     month = start.month
#     # 遍历月份数+1,之所以加1是因为即使是本月注册的博主，月份差为0，他的页面也要显示一个月，即本月
#     temp = []
#     for m in range(month_num + 1):
#         # 把年月的小列表追加进大列表
#         time_list.append(str(month) + '月')
#         temp.append(LF(year, month))
#         # 月份加1
#         month += 1
#         # 当月份达到13的时候，需要再从1月开始数，而且这代表跨年了，所以年份加1
#         if month == 13:
#             month = 1
#             year += 1
#     return time_list,temp

# time_list,temp = halfYear()
# print(time_list)
# print(temp)
# count_list = []
#
# for v in temp:
#     count = Schedule.query.filter(Schedule.start_time.between(v[0],v[1])).count()
#     count_list.append(count)
# print(count_list)

# def getTodayDate():
#     now = datetime.datetime.now()
#     zero_today = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
#                                           microseconds=now.microsecond)
#     last_today = zero_today + datetime.timedelta(hours=23, minutes=59, seconds=59)
#     return zero_today, last_today
# tomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
# print(tomorrowTime)
# now = datetime.datetime.now()
# zero_today = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
#                                       microseconds=now.microsecond)
# last_today = zero_today + datetime.timedelta(hours=23, minutes=59, seconds=59)
#
# tomorrow = now + datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
#                                     microseconds=now.microsecond)
# zero_tomorrow = tomorrow - datetime.timedelta(hours=tomorrow.hour, minutes=tomorrow.minute, seconds=tomorrow.second,
#                                               microseconds=tomorrow.microsecond)
# last_tomorrow = zero_tomorrow + datetime.timedelta(hours=23, minutes=59, seconds=59)
# print(last_tomorrow)

# t = Expense.query.all()
# expense_in = 0
# expense_out = 0
# for v in t:
#     if v.expense_type.type == '收入':
#         expense_in += int(v.money)
#     else:
#         expense_out += int(v.money)
# k = Schedule.query.all()
# for i in k:
#     money = int(i.money) - int(i.driver_money)
#     expense_in += money
# print(expense_in,expense_out)
# print(10-20)

# def getBetweenDay(start_date,end_date):
#   date_list = []
#   begin_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
#   end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
#   while begin_date <= end_date:
#     date_str = begin_date.strftime("%Y-%m-%d")
#     date_list.append(date_str)
#     begin_date += datetime.timedelta(days=1)
#   return date_list
#
# list = getBetweenDay('2019-04-01','2020-04-10')
# for v in list:
#   str = v + ' 00:00:00'
#   start = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
#   end = start + datetime.timedelta(hours=23, minutes=59, seconds=59)
#   print(start,end)
schedule = Schedule.query.filter_by(id=9).first_or_404()
track = Track.query.filter_by(id=schedule.track_id).first_or_404()
data = []
str = schedule.start_point + "->" + schedule.end_point
data.append({"name":str,"path":json.loads(track.steps)})