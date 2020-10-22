import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats
import os
import sys
import pandas as pd
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "20201008 계측 Data")
save_path = os.path.dirname(__file__)
sys.path.append(data_path)
plt.rcParams["font.family"] = "Times New Roman"

data = pd.read_csv(data_path+"\\1MOhm_closetoground_temperature.csv", skiprows=14, usecols=np.r_[0:3])
V_DUT = data.loc[:,'Channel 1 (V)'].to_list()
V_tot = data.loc[:,'Channel 2 (V)'].to_list()
T = data.loc[:, 'Time (s)'].to_list()

# choose what to use as x and y
x = np.array(list(T))
y = np.array(list(V_DUT))
x -= np.min(x)

# 무엇을 x와 y의 값에 얼마를 곱할 것인지 선택하라.(ex choose mV in x axis --> x_mul = 1e3) 
# 그래프에서 단위를 표기하는 것에 주의하라.
x_mul = 1e0
y_mul = 1e3
x_rlim = max(x)
x_llim = min(x)

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print('y = (%f) + (%f) * x' % (intercept, slope))
print('r^2 = %f' % r_value**2)
print('R_DUT = ', slope)
x_reggression = np.linspace(x_llim, x_rlim, 10)
y_reggression = intercept + slope * x_reggression

#average the results
x_avg = []
y_avg = []
avg_N = 10
for i in range(len(x)//avg_N):
    x_a = 0
    y_a = 0
    for j in range(avg_N):
        x_a += x[i*avg_N+j]
        y_a += y[i*avg_N+j]
    x_avg.append(x_a/avg_N)
    y_avg.append(y_a/avg_N)
x = x_avg
y = y_avg

#resize for plotting
x = [x_mul*e for e in x]
y = [y_mul*e for e in y]
x_reggression = [x_mul*e for e in x_reggression]
y_reggression = [y_mul*e for e in y_reggression]

x_rlim = max(x)
x_llim = min(x)
y_ulim = max(y)*1.1
y_dlim = 0#min(y)

plt.rc('font', size = 15)
plt.title('Curve between $\mathrm{t}$ and $\mathrm{V_{DUT}}$')
plt.xlabel('$t$[s]')
plt.ylabel('$\mathrm{V_{DUT}}$[mV]')
plt.xlim(x_llim, x_rlim)
plt.ylim(y_dlim, y_ulim)
plt.plot(x, y, color = 'black')
#plt.plot(x_reggression, y_reggression, label='fitted', color = 'blue', linewidth = 2)
plt.annotate('a', (x[30]+1, y[30]+0.3), color = 'blue', size = 20)
plt.plot(x[30], y[30], 'o', markersize = 5, color = 'blue')
plt.annotate('b', (x[170]-9, y[170]+0.25), color = 'blue', size = 20)
plt.plot(x[170], y[170], 'o', markersize = 5, color = 'blue')
plt.annotate('c', (x[323]-5, y[323]-0.8), color = 'blue', size = 20)
plt.plot(x[323], y[323], 'o', markersize = 5, color = 'blue')
plt.annotate('d', (x[375]+3, y[375]), color = 'blue', size = 20)
plt.plot(x[375], y[375], 'o', markersize = 5, color = 'blue')
plt.annotate('e', (x[430]-2, y[430]+0.3), color = 'blue', size = 20)
plt.plot(x[430], y[430], 'o', markersize = 5, color = 'blue')
#plt.show() 하면 pdf출력이 안됨. 왜그런지는 모르겠음
plt.savefig(os.path.join(save_path,'ICE_coolign_Vt.pdf'))
plt.show()