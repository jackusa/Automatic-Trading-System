 # -*- coding: utf-8 -*-

from requestGet import requestGet
from url import getURL
from split import split
from str2data import str2data

import win32api, win32con
from mouseCursor import click
from keyStroke import keyPress

code = '002407'
strings = split(requestGet(getURL(code)))
price = str2data(strings)

print price.close()
