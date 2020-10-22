"""
   DWF Python Example
   Author:  Digilent, Inc.
   Revision:  2018-07-19

   Requires:                       
       Python 2.7, 3
"""
#@
from matplotlib import pyplot as plt
from ctypes import *
import time
from dwfconstants import *
import sys
import matplotlib.pyplot as plt
import numpy
import numpy as np
import os
import pandas as pd

PARENT_PATH = os.path.dirname(__file__)
print(PARENT_PATH)
expname = 'exp2.2capacitance'

if sys.platform.startswith("win"):
    dwf = cdll.dwf
elif sys.platform.startswith("darwin"):
    dwf = cdll.LoadLibrary("/Library/Frameworks/dwf.framework/dwf")
else:
    dwf = cdll.LoadLibrary("libdwf.so")

version = create_string_buffer(16)
dwf.FDwfGetVersion(version)
print("Version: "+str(version.value))

cdevices = c_int()
dwf.FDwfEnum(c_int(0), byref(cdevices))
print("Number of Devices: "+str(cdevices.value))

if cdevices.value == 0:
    print("no device detected")
    quit()
#@

buffer_size = 8000


print("Opening first device")
hdwf = c_int()
dwf.FDwfDeviceOpen(c_int(0), byref(hdwf))

if hdwf.value == hdwfNone.value:
    print("failed to open device")
    quit()

def set_sine_output(frequency, Amplitude):
    print("Configure and start first analog out channel")
    dwf.FDwfAnalogOutEnableSet(hdwf, c_int(0), c_int(1)) # 1 = Sine wave")
    dwf.FDwfAnalogOutFunctionSet(hdwf, c_int(0), c_int(1))
    dwf.FDwfAnalogOutFrequencySet(hdwf, c_int(0), c_double(frequency))
    dwf.FDwfAnalogOutAmplitudeSet(hdwf, c_int(), c_double(Amplitude))
    dwf.FDwfAnalogOutConfigure(hdwf, c_int(0), c_int(1))

channel = c_int(0)
def set_square_output(frequency, Amplitude):
    print("Configure and start first analog out channel")
    #set power supply---------------------------------------------------------------------------------
    dwf.FDwfAnalogOutNodeEnableSet(hdwf, channel, AnalogOutNodeCarrier, c_bool(True))
    #funcDC, funcSine, funcSquare, funcTriangle, funcRampUp, funcRampDown, funcNoise, funcCustom, funcPlay
    dwf.FDwfAnalogOutNodeFunctionSet(hdwf, channel, AnalogOutNodeCarrier, funcSquare)
    dwf.FDwfAnalogOutNodeFrequencySet(hdwf, channel, AnalogOutNodeCarrier, c_double(frequency))
    dwf.FDwfAnalogOutNodeAmplitudeSet(hdwf, channel, AnalogOutNodeCarrier, c_double(amplitude))
    dwf.FDwfAnalogOutNodeOffsetSet(hdwf, channel, AnalogOutNodeCarrier, c_double(0.))
    dwf.FDwfAnalogOutConfigure(hdwf, channel, c_bool(True))
    '''
    dwf.FDwfAnalogOutEnableSet(hdwf, c_int(0), funcSquare) # 2 = square wave")
    dwf.FDwfAnalogOutFunctionSet(hdwf, c_int(0), funcSquare)
    dwf.FDwfAnalogOutFrequencySet(hdwf, c_int(0), c_double(frequency))
    dwf.FDwfAnalogOutAmplitudeSet(hdwf, c_int(), c_double(Amplitude))
    dwf.FDwfAnalogOutConfigure(hdwf, c_int(0), c_int(1))
    '''
    
cSamples = 1000
rgdSamples = (c_double*cSamples)()
channel = c_int(0)
# samples between -1 and +1
for i in range(0,len(rgdSamples)//2):
    rgdSamples[i] = 1.0
    rgdSamples[i+len(rgdSamples)//2] = -1.0

def set_custom_output(frequency, Amplitude):
    print("Configure and start first analog out channel")
    #set power supply---------------------------------------------------------------------------------
    dwf.FDwfAnalogOutNodeEnableSet(hdwf, channel, AnalogOutNodeCarrier, c_bool(True))
    #funcDC, funcSine, funcSquare, funcTriangle, funcRampUp, funcRampDown, funcNoise, funcCustom, funcPlay
    dwf.FDwfAnalogOutNodeFunctionSet(hdwf, channel, AnalogOutNodeCarrier, funcCustom)
    dwf.FDwfAnalogOutNodeDataSet(hdwf, channel, AnalogOutNodeCarrier, rgdSamples, c_int(cSamples))
    dwf.FDwfAnalogOutNodeFrequencySet(hdwf, channel, AnalogOutNodeCarrier, c_double(frequency))
    dwf.FDwfAnalogOutNodeAmplitudeSet(hdwf, channel, AnalogOutNodeCarrier, c_double(amplitude))
    dwf.FDwfAnalogOutNodeOffsetSet(hdwf, channel, AnalogOutNodeCarrier, c_double(0.))
    dwf.FDwfAnalogOutConfigure(hdwf, channel, c_bool(True))


def set_analog_input(measure_frequency):
    print("Configure analog in")
    dwf.FDwfAnalogInFrequencySet(hdwf, c_double(measure_frequency))
    print("Set range for all channels")
    dwf.FDwfAnalogInChannelRangeSet(hdwf, c_int(-1), c_double(20))
    dwf.FDwfAnalogInBufferSizeSet(hdwf, c_int(buffer_size))

print("Wait after first device opening the analog in offset to stabilize")
time.sleep(2)

Resistance = 220
capacitance = 1e-7
Period_data_num = 1000
frequency = 10000
measure_freq = frequency * Period_data_num
amplitude = 5
#set_custom_output(frequency, amplitude)
set_sine_output(frequency, amplitude)
set_analog_input(measure_freq)

print("Wait after generate wave")
time.sleep(2)

print("Starting acquisition...")
dwf.FDwfAnalogInConfigure(hdwf, c_int(1), c_int(1))

sts = c_int()
while True:
    dwf.FDwfAnalogInStatus(hdwf, c_int(1), byref(sts))
    if sts.value == DwfStateDone.value :
        break
    time.sleep(0.1)
print("   done")

rg1 = (c_double*buffer_size)()
rg2 = (c_double*buffer_size)()

dwf.FDwfAnalogInStatusData(hdwf, c_int(0), rg1, len(rg1)) # get channel 1 data
dwf.FDwfAnalogInStatusData(hdwf, c_int(1), rg2, len(rg2)) # get channel 2 data

dwf.FDwfAnalogOutReset(hdwf, c_int(0))
dwf.FDwfDeviceCloseAll()

V1_np = numpy.fromiter(rg1, dtype = numpy.float).tolist()
V2_np = numpy.fromiter(rg2, dtype = numpy.float).tolist()

#save _df to csv file
t = (np.arange(len(V1_np))/measure_freq).tolist()
tutorial_df = pd.DataFrame({'time' : t, 'V1' : V1_np, 'V2' : V2_np, 'sineoutput_freq' : frequency, 'sineoutput_amplitude':amplitude, 'Resistance':Resistance, 'capacitance': capacitance})
tutorial_df.to_csv(os.path.join(PARENT_PATH, expname+'freq'+str(frequency)+'amp'+str(amplitude)+'.csv'))

plt.plot(numpy.fromiter(rg1, dtype = numpy.float), numpy.fromiter(rg2, dtype = numpy.float))

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()
