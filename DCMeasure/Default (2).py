from matplotlib import pyplot as plt
import time
import os
import sys
import math
import pandas as pd
PARENT_PATH = os.path.dirname(__file__)
sys.path.append(os.path.dirname(PARENT_PATH))
from ctypes import *
from py.dwfconstants import *
#----------------------------measure time, # of samples---------------------
SLEEP_TIME=0.01
SAMPLES=100
#-------------------------------------------------------

dwf = cdll.dwf
hdwf = c_int()

channel = c_int(0)
hzSys = c_double()
voltage0 = c_double()
voltage1 = c_double()
version = create_string_buffer(16)
dwf.FDwfGetVersion(version)
print("DWF Version: "+str(version.value))
print ("Opening first device...")
dwf.FDwfDeviceOpen(c_int(-1), byref(hdwf))
if hdwf.value == hdwfNone.value:
 print ("failed to open device")
 quit()



dwf.FDwfDigitalOutInternalClockInfo(hdwf, byref(hzSys))
print ("Note the internal clock frequency")
print ("the internal clock frequency is "+str(hzSys.value))
print ("preparing to read sample...")
print ("Note the voltage for the bright light that your sensor will see")
print ("Note the voltage for the darkest light that your sensor will see")

dwf.FDwfAnalogIOChannelNodeSet(hdwf, c_int(0), c_int(0), c_double(True))
dwf.FDwfAnalogIOEnableSet(hdwf, c_int(True))


dwf.FDwfAnalogInChannelEnableSet(hdwf, c_int(0), c_bool(True))
dwf.FDwfAnalogInChannelOffsetSet(hdwf, c_int(0), c_double(0))
dwf.FDwfAnalogInChannelRangeSet(hdwf, c_int(-1), c_double(0.2))
dwf.FDwfAnalogInConfigure(hdwf, c_bool(False), c_bool(False))



#set power supply---------------------------------------------------------------------------------
Power_V_list = [5*i/SAMPLES for i in range(SAMPLES+1)]
    
#-------------------------------------------------------------------------------------------------

time.sleep(2)




for i in range(SAMPLES+1):
    dwf.FDwfAnalogIOChannelNodeSet(hdwf, c_int(0), c_int(1), c_double(Power_V_list[i]))
    time.sleep(SLEEP_TIME)
    dwf.FDwfAnalogInStatus(hdwf, False, None)


    dwf.FDwfAnalogInStatusSample(hdwf, c_int(0), byref(voltage0))   #oscilloscope 0
    dwf.FDwfAnalogInStatusSample(hdwf, c_int(1), byref(voltage1))   #oscilloscope 1

    
    print ("voltage0, voltage1 = {:.5f}, {:.5f}".format(voltage0.value, voltage1.value))


#------------------------------
#save _df to csv file
#tutorial_df = pd.DataFrame({'time_list' : time_list, 'V0_list' : V0_list, 'V1_list1' : V1_list})
#tutorial_df.to_csv(os.path.join(PARENT_PATH, 'tutorial_df.csv'))



plt.plot(Power_V_list, Power_V_list, label = 'Power_V_list')
plt.plot(Power_V_list, V0_list, label = 'V0_list')
plt.plot(Power_V_list, V1_list, label = 'V1_list')
plt.legend()
plt.show()
dwf.FDwfDigitalOutReset(hdwf)
dwf.FDwfDeviceCloseAll()
