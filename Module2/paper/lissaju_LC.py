#보류
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats
import os
import sys
import pandas as pd
from matplotlib.pyplot import errorbar
data_path = os.path.dirname(os.path.dirname(__file__))
save_path = os.path.dirname(__file__)
sys.path.append(data_path)
plt.rcParams["font.family"] = "Times New Roman"

data = pd.read_csv(data_path+"\\exp2.2ind_capfreq10000amp5.csv")

time = np.array(list(data['time']))
V1 = np.array(list(data['V1']))
V2 = np.array(list(data['V2']))
sineoutput_freq = list(data['sineoutput_freq'])[0]
sineoutput_amplitude = list(data['sineoutput_amplitude'])[0]

#x = I, y = time

y = V1
x = V2

print("maxV1 = ", max(V1))
print("maxV2 = ", max(V2))
maxv1 = 0
maxv2 = []
for i, v1 in enumerate(V1):
    if(abs(v1)<0.01) and V2[i]>0:
        maxv2.append(V2[i])

Y_U = np.average(np.array(maxv2))
X_U = maxv1
print("V1 max --> V2 = ", Y_U)


maxv1 = 0
maxv2 = []
for i, v1 in enumerate(V1):
    if(abs(v1)<0.01) and V2[i]<0:
        maxv2.append(V2[i])

Y_D = np.average(np.array(maxv2))
X_D = maxv1
print("V1 max --> V2 = ", Y_D)
print('delta = ', np.arcsin((-Y_D+Y_U)/2/max(V2)), '[rad]')

# 무엇을 x와 y의 값에 얼마를 곱할 것인지 선택하라.(ex choose mV in x axis --> x_mul = 1e3) 
# 그래프에서 단위를 표기하는 것에 주의하라.
x_mul = 1
y_mul = 1
x_rlim = max(x)
x_llim = min(x)

x = V1
y = V2


#resize for plotting
x = [x_mul*e for e in x]
y = [y_mul*e for e in y]

plt.rc('font', size = 13)

plt.title('Curve between $V_C$ and $V_L$')
plt.xlabel('$V_C$[$V$]')
plt.ylabel('$V_L$[$V$]')
#plt.xlim(x_llim, x_rlim)
#plt.ylim(y_dlim, y_ulim)
plt.plot(x, y,'.', label='experiment', markersize = 2, color = 'black')
errorbar(X_U, Y_U, label='y+ intercept', yerr = 0.06,  xerr = 0.01, fmt="ro-",ecolor='red', capthick=1, capsize=3, markersize = 4)
errorbar(X_D, Y_D, label='y- intercept',yerr = 0.02,  xerr = 0.01, fmt="bo-",ecolor='blue', capthick=1, capsize=3, markersize = 4)
plt.legend(loc=0)
plt.savefig(os.path.join(save_path,'Lissaju_LC.pdf'))
plt.show()