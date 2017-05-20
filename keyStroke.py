# Firstly, install 'SendKeys-0.3-cp27-none-win32.whl'
import SendKeys 
import time

#https://xueqiu.com/4477733530/43467462
# http://win32com.goermezer.de/microsoft/windows/controlling-applications-via-sendkeys.html
def keyPress():
    try:
        sendMe = "1"
        time.sleep(30)
        SendKeys.SendKeys(sendMe)
        # SendKeys.SendKeys("{ENTER}")

    except Exception, e:
        print str(e)





