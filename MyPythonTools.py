import os
#import sys #需要在macOS和各Linux之间区分的时候使用sys.platform

def isWindows():
    return os.name == 'nt'

def isPosix():
    return os.name == 'posix'

def convertUtf8ToGBK(file_position):
    f_open  = open(str(file_position), 'rb')
    f_bytes = bytes(f_open.read())
    f_open.close()
    return f_bytes.decode('gbk')

def getADBScreenSize():
    os.system('adb shell wm size > size')
    with open('size', 'r') as f:
        s = f.read()
    return s