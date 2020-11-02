#보류
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats
import os
import sys
import pandas as pd
from matplotlib.pyplot import errorbar
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'opampdata')
save_path = os.path.dirname(__file__)
sys.path.append(data_path)
plt.rcParams["font.family"] = "Times New Roman"

data = pd.read_csv(data_path+"\\Module2sine_2kHz_capa양단.csv", skiprows=28)

data_start = 8
data_end = 1000
time = np.array(list(data['Time (s)']))
V1 = np.array(list(data['Channel 1 (V)']))
V2 = np.array(list(data['Channel 2 (V)']))
R1 = 1e6
C = 1e-9

#적분 파동
#x = I, y = time

y = V1[data_start:data_end]
x = time[data_start:data_end]

x_mul = 1000
y_mul = 1
x_rlim = max(x)
x_llim = min(x)

def integrate(A, time, data_start = data_start, data_end = data_end):
    ret = []
    sum = 0
    for i in range(len(A)-1):
        sum+=A[i]*(time[i+1]-time[i])
        ret.append(sum)
    return np.array(ret)[data_start:data_end]
integrate = integrate(V2, time)*(-1/R1/C)

add_0 = ((max(V1)+min(V1))-(max(integrate)+min(integrate)))/2
integrate += add_0

#resize for plotting
x = [x_mul*e for e in x]
y = [y_mul*e for e in y]
integrate = [y_mul*e for e in integrate]

plt.rc('font', size = 13)

plt.title('Comparison of $V_{o}$ and $\int -V_{in}/RC dt$')
plt.xlabel('$t$[$ms$]')
plt.ylabel('$V$[$V$]')
#plt.xlim(x_llim, x_rlim)
#plt.ylim(y_dlim, y_ulim)
plt.plot(x, y,'.', label='$V_{o}$', markersize = 2, color = 'red')
plt.plot(x, integrate,'.', label='$\int -V_{in}/RC dt$', markersize = 2, color = 'blue')
plt.legend(loc=0)
plt.savefig(os.path.join(save_path,'opamp_integrate_sine_cap.pdf'))
plt.show()


print("max V1 = ", max(y))
print("max integrate = ", max(integrate))
#그냥 파동
#x = I, y = time

y = V2[data_start:data_end]
x = time[data_start:data_end]

x_mul = 1000
y_mul = 1
x_rlim = max(x)
x_llim = min(x)


#resize for plotting
x = [x_mul*e for e in x]
y = [y_mul*e for e in y]


plt.title('Curve between $t$ and $V_{original}$')
plt.xlabel('$t$[$ms$]')
plt.ylabel('$V_{original}$[$V$]')
#plt.xlim(x_llim, x_rlim)
#plt.ylim(y_dlim, y_ulim)
plt.plot(x, y,'.', label='original', markersize = 2, color = 'black')
plt.legend(loc=0)
plt.savefig(os.path.join(save_path,'opamp_original_sine_cap.pdf'))
plt.show()