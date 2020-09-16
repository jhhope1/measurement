from ctypes import *
from dwfconstants import *
import sys
import time

if sys.platform.startswith("win"):
    dwf = cdll.dwf
elif sys.platform.startswith("darwin"):
    dwf = cdll.LoadLibrary("libdwf.dylib")
else:
    dwf = cdll.LoadLibrary("libdwf.so")

hdwf = c_int()

#open device
print("Opening first device")
dwf.FDwfDeviceOpen(c_int(-1), byref(hdwf))
# To automatically enumerate all connected devices and open the first discovered device, use index -1.
# 왜 0이 안되는지는 모르겠습니다.
if hdwf.value == hdwfNone.value:
    print("failed to open device")
    quit()

# c기반으로 되어있고, 거의 모든 함수가 포인터를 기반으로 만들어져있어서 c_int를 만들고 byref()를 통해 포인터를 인자로 넘겨야한다.
a = c_int()
#UsbPower enable = 1, disable = 0
dwf.FDwfParamSet(c_int(1), 1)
dwf.FDwfParamGet(c_int(1), byref(a))
print(a)

#LED brightness 50% DwfParamLedBrightness = c_int(3)
dwf.FDwfParamSet(DwfParamLedBrightness, 50)
dwf.FDwfParamGet(c_int(3), byref(a))
print(a)#c_long(50)

#get list of detected devices
dwf.FDwfEnum(c_int(0), byref(a))
print(a.value)#1


#get user name

user_name = create_string_buffer(16)
dwf.FDwfEnumUserName(c_int(0), user_name)
print(user_name.value)#b'Discovery2'

#FDwfEnumConfig
pcConfig = c_int()
dwf.FDwfEnumConfig(c_int(0), byref(pcConfig))
print(pcConfig.value)#7

#FDwfEnumConfigInfo
channel_count = c_int()
dwf.FDwfEnumConfigInfo(0, DECIDigitalOutChannelCount, byref(channel_count))
print(channel_count.value)#16: 아마도 0~15를 말하는듯..?

#close device
dwf.FDwfDeviceCloseAll()


a = 1