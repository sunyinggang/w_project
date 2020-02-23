<?php
$idcard = "370826200710014638";
$date = strtotime(substr($idcard,6,8));

#  获得今日的时间戳

$today = strtotime('today');

#  得到两个日期相差的大体年数

$diff = floor(($today-$date)/86400/365);

#  strtotime加上这个年数后得到那日的时间戳后与今日的时间戳相比

$age = strtotime(substr($idcard,6,8).' +'.$diff.'years')>$today?($diff+1):$diff;
print($age);