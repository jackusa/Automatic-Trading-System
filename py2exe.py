 # -*- coding: utf-8 -*-
 
from cx_Freeze import setup, Executable

setup(name = 'ats',
    version = '0.1',
    description = 'executatable file',
    executables = [Executable('test.py')]
    )