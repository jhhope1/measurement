from matplotlib import pyplot as plt
import time
import os
import sys
import math
import pandas as pd
from ctypes import *
from const import *
#add dir path to system path
sys.path.append(os.path.dirname(PARENT_PATH))
from py.dwfconstants import *

#@아래는 dwf(digilent waveforms)를 불러오고 device를 연결하는 내용
# using windows plateform
dwf = cdll.dwf
#declare ctype variables
hdwf = c_int()

#asdfkdjeos

#channel 0이 V+-, channel 1이 W+-인듯 합니다.
channel = c_int(1)
hzSys = c_double()
voltage0 = c_double()
voltage1 = c_double()
#print DWF version
version = create_string_buffer(16)
dwf.FDwfGetVersion(version)
print("DWF Version: "+str(version.value))
#open device
print ("Opening first device...")
dwf.FDwfDeviceOpen(c_int(-1), byref(hdwf))
if hdwf.value == hdwfNone.value:
 print ("failed to open device")
 quit()
#@

sine = True
DC = False


#-------------------------------------------------
#The function FDwfDigitalOutInternalClockInfo is used to retrieve the internal clock frequency.
#and store frequency in variable hzSys
dwf.FDwfDigitalOutInternalClockInfo(hdwf, byref(hzSys))
print ("Note the internal clock frequency")
print ("the internal clock frequency is "+str(hzSys.value))
print ("preparing to read sample...")
print ("Note the voltage for the bright light that your sensor will see")
print ("Note the voltage for the darkest light that your sensor will see")

#supply를 할거냐 + 어떻게 할거냐 + 얼마나 할거냐. pdf설명이 너무 부실하니 examples를 같이 보면 좋을 것 같습니다.(example도 설명은 부실하나 베껴쓰면 됩니다.)
#https://forum.digilentinc.com/topic/3551-waveforms-sdk-identification-of-channels-and-nodes/
#(hdwf, c_int(0) --> positive supply, c_int(0)-->enable?, c_double(True)-->Yes) 
# enable positive supply
dwf.FDwfAnalogIOChannelNodeSet(hdwf, c_int(0), c_int(0), c_double(True))
# master enable 마스터가 뭔지는 잘 모르겠어요.. DC할때는 필요한 것 같은데 AC로 할때는 상관이 없는것 같습니다.
dwf.FDwfAnalogIOEnableSet(hdwf, c_int(True))


#--Set up analog input on channel 1---------------
dwf.FDwfAnalogInChannelEnableSet(hdwf, c_int(0), c_bool(True))
dwf.FDwfAnalogInChannelOffsetSet(hdwf, c_int(0), c_double(0))
dwf.FDwfAnalogInChannelRangeSet(hdwf, c_int(-1), c_double(5))
dwf.FDwfAnalogInConfigure(hdwf, c_bool(False), c_bool(False))
# 왜 안해도 문제 없는지는 모르겠음...?bb..

#set power supply
Power_V_list = [i/SAMPLES*V_max for i in range(SAMPLES+1)]

#wait for stabilize
time.sleep(2)
#1MHz단위로 acquisition이 가능하다고 합니다. 앞으로 out_in은 AnalogInOut sample을 보면서 하면 될 것 같습니다. 
Oscillo1_list = []
Oscillo2_list = []

for i in range(SAMPLES+1):
    #(hdwf, c_int(0) --> positive supply, c_int(0)-->setting exact value?, c_double(Power_V) --> set V to Power_V)
    dwf.FDwfAnalogIOChannelNodeSet(hdwf, c_int(0), c_int(1), c_double(Power_V_list[i]))
    time.sleep(SLEEP_TIME)
    #이걸 안해주면 측정이 안되니 해야할것 같습니다.. False일때가 뭔진 모르겠으나 예제에 나와있었고, acquisition을 해주는 것 같습니다.
    # Checks the state of the acquisition. To read the data from the device, set fReadData to TRUE. For-
    # single acquisition mode, the data will be read only when the acquisition is finished.
    dwf.FDwfAnalogInStatus(hdwf, False, None)

    # Gets the last ADC(Analog to digital) conversion sample from the specified idxChannel on the AnalogIn instrument.
    dwf.FDwfAnalogInStatusSample(hdwf, c_int(0), byref(voltage0))   #oscilloscope 0
    # Gets the last ADC(Analog to digital) conversion sample from the specified idxChannel on the AnalogIn instrument.
    dwf.FDwfAnalogInStatusSample(hdwf, c_int(1), byref(voltage1))   #oscilloscope 1

    Oscillo1_list.append(voltage0.value)
    Oscillo2_list.append(voltage1.value)
    print ("voltage0, voltage1 = {:.5f}, {:.5f}".format(voltage0.value, voltage1.value))
#------------------------------

#save _df to csv file
tutorial_df = pd.DataFrame({'Power_V_list' : Power_V_list, 'Oscillo1_list' : Oscillo1_list, 'Oscillo2_list' : Oscillo2_list})
tutorial_df.to_csv(os.path.join(PARENT_PATH, 'Load_Rangeon.csv'))

#plt.plot(Power_V_list, Power_V_list, label = 'Power_V_list')
plt.plot(Power_V_list, Oscillo1_list, label = 'Oscillo1_list_range_off')
#plt.plot(Power_V_list, Oscillo2_list, label = 'Oscillo2_list')
#실험 결과 확인할 때 좋을 것 같습니다.
plt.legend()
plt.show()
dwf.FDwfDigitalOutReset(hdwf)
dwf.FDwfDeviceCloseAll()
