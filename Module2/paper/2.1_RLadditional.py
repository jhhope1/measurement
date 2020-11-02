#보류
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats
import os
import sys
import pandas as pd
data_path = os.path.dirname(os.path.dirname(__file__))
save_path = os.path.dirname(__file__)
sys.path.append(data_path)
plt.rcParams["font.family"] = "Times New Roman"

data = pd.read_csv(data_path+"\\exp2.2.2freq44amp5.csv")

time = np.array(list(data['time']))
V1 = np.array(list(data['V1']))
V2 = np.array(list(data['V2']))
sineoutput_freq = list(data['sineoutput_freq'])[0]
sineoutput_amplitude = list(data['sineoutput_amplitude'])[0]

x = time
y = V1

# 무엇을 x와 y의 값에 얼마를 곱할 것인지 선택하라.(ex choose mV in x axis --> x_mul = 1e3) 
# 그래프에서 단위를 표기하는 것에 주의하라.
x_mul = 1e-3
y_mul = 1
V0 = abs(np.average(y[90:100]))
print("average_V0 = ", V0)


x = x[:len(x)//5]
y = y[:len(y)//5]
V2 = V2[:len(V2)//5]

#밀고 다시 짜기

#fitted line
s = 300
e = 330
fit_x = time[s:e]
fit_y = V1[s:e]
fit_V2 = V2[s:e]
Vs = fit_V2-fit_y
DVs = (Vs[2:] - Vs[:-2])/(fit_x[2:]-fit_x[:-2])

RL = 137.62632486204325
Rtot = RL+220
y = (fit_y-RL/Rtot*fit_V2)[1:-1]
x = DVs


x_rlim = max(x)
x_llim = min(x)

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print('y = (%f) + (%f) * x' % (intercept, slope))
print('r^2 = %f' % r_value**2)
print('tau = ', slope)
x_reggression = np.linspace(x_llim, x_rlim, 10)
y_reggression = intercept + slope * x_reggression

#resize
x = [x_mul*e for e in x]
y = [y_mul*e for e in y]
x_reggression = [x_mul*e for e in x_reggression]
y_reggression = [y_mul*e for e in y_reggression]


x_rlim = max(x)
x_llim = min(x)
y_ulim = max(y)
y_dlim = min(y)

plt.rc('font', size = 13)

plt.title('Curve between $V_{in}-V_C$ and $\mathrm{\dot{V_C}}$')
plt.xlabel('$\mathrm{\dot{V_C}}[kV/s$]')
plt.ylabel('$V_{in}-V_C$[V]')
#plt.xlim(x_llim, x_rlim)
#plt.ylim(y_dlim, y_ulim)
plt.plot(x_reggression, y_reggression, label='fitted', linewidth = 2, color = 'blue')
plt.plot(x, y,'.', label='experiment', markersize = 7, color = 'black')
plt.legend(loc=0)
plt.savefig(os.path.join(save_path,'RL_subV-DV_modify.pdf'))
plt.show()