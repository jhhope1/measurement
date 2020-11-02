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

data = pd.read_csv(data_path+"\\exp2.2capacitancefreq5000amp5.csv")

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

print("maxV1 = ", max(V1))
print("maxV2 = ", max(V2))
maxv1 = 0
maxv2 = []
for i, v1 in enumerate(V1):
    if maxv1 < v1:
        maxv2 = [V2[i]]
        maxv1 = v1
    if maxv1 == v1:
        maxv2.append(V2[i])

Y_R = np.average(np.array(maxv2))
X_R = maxv1
print("V1 max --> V2 = ", Y_R)
print('delta = ', np.arcsin(Y_R/max(V2)), '[rad]')

maxv1 = []
maxv2 = 0
for i, v2 in enumerate(V2):
    if maxv2 < v2:
        maxv1 = [V1[i]]
        maxv2 = v2
    if maxv2 == v2:
        maxv1.append(V1[i])
Y_U = maxv2
X_U = np.average(np.array(maxv1))
print(maxv1)
print("V2 max --> V1 = ", X_U)
print('delta = ', np.arcsin(X_U/max(V1)), '[rad]')



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

plt.title('Curve between $V_C$ and $V_R$')
plt.xlabel('$V_C$[$V$]')
plt.ylabel('$V_R$[$V$]')
#plt.xlim(x_llim, x_rlim)
#plt.ylim(y_dlim, y_ulim)
plt.plot(x, y,'.', label='experiment', markersize = 2, color = 'black')
errorbar(X_R, Y_R, label='rightmost', yerr = 0.3,  xerr = 0.1, fmt="ro-",ecolor='red', capthick=1, capsize=3, markersize = 4)
errorbar(X_U, Y_U, label='uppermost',yerr = 0.02,  xerr = 0.5, fmt="bo-",ecolor='blue', capthick=1, capsize=3, markersize = 4)
#plt.plot(x, y, '.', label='fitted part', markersize = 7, color = 'blue')
plt.legend(loc=0)
plt.savefig(os.path.join(save_path,'Lissaju_RC.pdf'))
plt.show()