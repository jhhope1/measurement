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

data = pd.read_csv(data_path+"\\1Mohm4단자osc.csv", skiprows=28, usecols=np.r_[0:3])
V_DUT = data.loc[:,'Channel 1 (V)'].to_list()
V_tot = data.loc[:,'Channel 2 (V)'].to_list()

# choose what to use as x and y
x = list(V_tot)
y = list(V_DUT)

# 무엇을 x와 y의 값에 얼마를 곱할 것인지 선택하라.(ex choose mV in x axis --> x_mul = 1e3) 
# 그래프에서 단위를 표기하는 것에 주의하라.
x_mul = 1.
y_mul = 1e3
x_rlim = max(x)
x_llim = min(x)

slope, intercept, r_value, p_value, std_err = stats.linregress(V_tot, V_DUT)
print('y = (%f) + (%f) * x' % (intercept, slope))
print('r^2 = %f' % r_value**2)
x_reggression = np.linspace(x_llim, x_rlim, 100)
y_reggression = intercept + slope * x_reggression

#resize for plotting
x = [x_mul*e for e in x]
y = [y_mul*e for e in y]
x_reggression = [x_mul*e for e in x_reggression]
y_reggression = [y_mul*e for e in y_reggression]

x_rlim = max(x)
x_llim = min(x)
y_ulim = max(y)
y_dlim = min(y)


plt.title('Correlation between $\mathrm{V_{tot}}$ and $\mathrm{V_{DUT}}$')
plt.xlabel('$\mathrm{V_{tot}}$[V]')
plt.ylabel('$\mathrm{V_{DUT}}$[mV]')
plt.xlim(x_llim, x_rlim)
plt.ylim(y_dlim, y_ulim)
plt.plot(x, y, '.', label='experiment', markersize = 1, color = 'black')
plt.plot(x_reggression, y_reggression, label='fitted', color = 'blue', linewidth = 2)
plt.legend(loc=0)
#plt.show() 하면 pdf출력이 안됨. 왜그런지는 모르겠음
#plt.show()
plt.savefig(os.path.join(save_path,'0_IV_curve_with_calibration.pdf'))