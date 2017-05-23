 # -*- coding: utf-8 -*-

from datetime import datetime

class workSchedule():
    def __init__(self):

        self.morningBegan = '09:30:01'
        self.morningEnd = '11:30:00'
        self.noonBegan = '13:00:01'
        self.noonEnd = '15:00:00'

        self.currentTime = datetime.now().strftime("%H:%M:%S") 
    
    def ifWork(self):
        if self.currentTime > self.morningBegan and self.currentTime < self.morningEnd:
            return True
        elif self.currentTime > self.noonBegan and self.currentTime < self.noonEnd:
            return True
        else:
            return False

    def ifIdle(self):
        if self.currentTime > self.morningEnd and self.currentTime < self.morningBegan:
            return True
        else:
            return False

    def ifEnd(self):
        if self.currentTime > self.noonEnd:
            return True
        else:
            return False


