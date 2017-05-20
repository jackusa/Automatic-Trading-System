import os
import sys

if len(sys.argv)>1:
    None
else:
    File = input("Choose the file you want to compile: ")
    print (File)
    # os.system("C:\Python34\Scripts\cxfreeze "+File)
    os.system('C:\totalcmd\TOTALCMD.EXE')
    print("Finish")