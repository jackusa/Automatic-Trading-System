 # -*- coding: utf-8 -*-
import sys
import time
from datetime import datetime 

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
myExcel = wrExcel(code, str(datetime.now().strftime("%y-%m-%d")))
myExcel.set()

cnt  = 1 # row number of excel 

while (not workSchedule().ifEnd()):
    
    if workSchedule().ifWork():
        
        if workSchedule().ifSample():
            dataStr = requestGet(getURL(code))
            dataList = split(dataStr)
            

            dateStr = dataList[-3]
            timeStr = dataList[-2]
            saveTXT(code, dateStr, timeStr, dataStr)
            myExcel.write(cnt, dataList)
            cnt  = cnt + 1

            price = str2data(dataList)
            
            print cnt
            time.sleep(1) 
            # The code began to run at XX:XX:00. But sometimes its work can be finished in 1 second. 
            # So I add a dealy time to avoid running code with multiple cycles in 1 second.
        else:
            pass
   
    else:
        pass

myExcel.save()
