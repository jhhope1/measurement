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

data = pd.read_csv(data_path+"\\exp2.2.1freq333.3333333333333amp1.csv")

time = np.array(list(data['time']))
V1 = np.array(list(data['V1']))
V2 = np.array(list(data['V2']))
sineoutput_freq = list(data['sineoutput_freq'])[0]
sineoutput_amplitude = list(data['sineoutput_amplitude'])[0]

#x = I, y = time

y = V1
x = time


# 무엇을 x와 y의 값에 얼마를 곱할 것인지 선택하라.(ex choose mV in x axis --> x_mul = 1e3) 
# 그래프에서 단위를 표기하는 것에 주의하라.
x_mul = 1e-3
y_mul = 1
V0 = abs(np.average(y[90:100]))
print("average_V0 = ", V0)


x = x[:len(x)//50]
y = y[:len(y)//50]
V2 = V2[:len(V2)//50]

#fitted line
s = 54
e = 70
fit_x = x[s:e]
fit_y = y[s:e]
V2 = V2[s:e]
DV = (fit_y[2:]-fit_y[:-2])/(fit_x[2:]-fit_x[:-2])
subV = V2-fit_y
y = subV[1:-1]
x = DV

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


x_rlim = max(x)*1.1
x_llim = min(x)*1.1
y_ulim = max(y)*1.1
y_dlim = min(y)*1.1

plt.rc('font', size = 13)

plt.title('Curve between $V_{in}-V_C$ and $\mathrm{\dot{V_C}}$')
plt.xlabel('$\mathrm{\dot{V_C}}[kV/s$]')
plt.ylabel('$V_{in}-V_C$[V]')
plt.xlim(x_llim, x_rlim)
plt.ylim(y_dlim, y_ulim)
plt.plot(x_reggression, y_reggression, label='fitted', linewidth = 2, color = 'blue')
plt.plot(x, y,'.', label='experiment', markersize = 7, color = 'black')
plt.legend(loc=0)
plt.savefig(os.path.join(save_path,'RC_subV-DV_modify.pdf'))
plt.show()