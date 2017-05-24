 # -*- coding: utf-8 -*-
import sys
import time 

from requestGet import requestGet
from url import getURL
from split import split
from str2data import str2data
from workSchedule import workSchedule

import win32api, win32con
from mouseCursor import click
from keyStroke import keyPress
from saveTXT import saveTXT
from saveExcel import wrExcel

reload(sys)                      
sys.setdefaultencoding('utf-8')

code = '002407'

while (not workSchedule().ifEnd()):
    cnt  = 1
    if not workSchedule().ifWork():
        
        if workSchedule().ifSample():
            dataStr = requestGet(getURL(code))
            dataList = split(dataStr)
            

            dateStr = dataList[-3]
            timeStr = dataList[-2]
            saveTXT(code, dateStr, timeStr, dataStr)
            wrExcel().write(code, dateStr, cnt, dataList)
            cnt  = cnt + 1

            price = str2data(dataList)
            
            print cnt

        else:
            pass
   
    else:
        pass


