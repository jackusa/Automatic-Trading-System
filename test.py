 # -*- coding: utf-8 -*-
import sys
import time 

from requestGet import requestGet
from url import getURL
from split import split
from str2data import str2data

import win32api, win32con
from mouseCursor import click
from keyStroke import keyPress
from saveTXT import saveTXT

reload(sys)                      
sys.setdefaultencoding('utf-8')

code = '002407'
dataStr = requestGet(getURL(code))

dataList = split(dataStr)
dateStr = dataList[-3]
timeStr = dataList[-2]

price = str2data(dataList)

for i in range(5):
    time.sleep(2)
    saveTXT(code, dateStr, timeStr, dataStr)

