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

#x = I, y = time

y = V1
x = time


# 무엇을 x와 y의 값에 얼마를 곱할 것인지 선택하라.(ex choose mV in x axis --> x_mul = 1e3) 
# 그래프에서 단위를 표기하는 것에 주의하라.
x_mul = 1000
y_mul = 1
V0 = np.average(y[:50])
V_input = np.average(V2[:50])
print("average_V0 = ", V0)
print("V_input = ", V_input)
print("RL = ", V0*220/(V_input-V0))

x_rlim = max(x)
x_llim = min(x)

x = x[:len(x)//9]
y = y[:len(y)//9]
V2 = V2[:len(V2)//9]


#fitted line
s = 300
e = 330
fit_x = x[s:e]
fit_y = y[s:e]
V2 = V2[s:e]
fit_y = np.log(-V0-fit_y)


#resize for plotting
x = [x_mul*e for e in x]
y = [y_mul*e for e in y]

x_rlim = max(x)
x_llim = min(x)
y_ulim = max(y)
y_dlim = min(y)


plt.rc('font', size = 13)
plt.title('Curve between $\mathrm{t}$ and $\mathrm{V_L}$')
plt.xlabel('$t$[$ms$]')
plt.ylabel('$V_L$[V]')
plt.xlim(x_llim, x_rlim)
plt.ylim(y_dlim, y_ulim)
plt.plot(x, y,'.', label='experiment', markersize = 5, color = 'black')
plt.plot(x[s:e], y[s:e], '.', label='fitted part', markersize = 7, color = 'blue')
plt.legend(loc=0)
plt.savefig(os.path.join(save_path,'RL_V-t_curve.pdf'))
plt.show()


#fitted lien plot

#resize for plotting
x = fit_x
y = fit_y
slope, intercept, r_value, p_value, std_err = stats.linregress(fit_x, fit_y)
print('y = (%f) + (%f) * x' % (intercept, slope))
print('r^2 = %f' % r_value**2)
print('R_DUT = ', slope)
print('tau = ', -1/slope)
x_reggression = np.linspace(x_llim, x_rlim, 10)
y_reggression = intercept + slope * x_reggression

x_mul = 1000
y_mul = 1
x = [x_mul*e for e in x]
y = [y_mul*e for e in y]
x_reggression = [x_mul*e for e in x_reggression]
y_reggression = [y_mul*e for e in y_reggression]



x_rlim = max(x)*1.02
x_llim = min(x)*0.98
y_ulim = max(y)*1.1
y_dlim = min(y)*1.1


plt.title('Correlation between $t$ and $log(-V_{in}-V_L)$')
plt.xlabel('$t$[$ms$]')
plt.ylabel('$log(-V_{in}-V_L)[-]$')
plt.xlim(x_llim, x_rlim)
plt.ylim(y_dlim, y_ulim)
plt.plot(x_reggression, y_reggression, label='fitted', color = 'blue', linewidth = 2)
plt.plot(x, y,'.', label='experiment', markersize = 6, color = 'black')
plt.legend(loc=0)
plt.savefig(os.path.join(save_path,'RL_log(V-V0)-t_correlation.pdf'))
plt.show()
