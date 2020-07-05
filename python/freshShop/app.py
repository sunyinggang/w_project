#encoding = utf-8
import datetime,random

nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")#当前时间
str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"+nowTime
sa = []
for i in range(26):
    sa.append(random.choice(str))
salt = ''.join(sa)

