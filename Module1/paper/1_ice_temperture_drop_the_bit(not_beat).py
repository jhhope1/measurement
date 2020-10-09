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

data = pd.read_csv(data_path+"\\1MOhm_얼음추가_빼기.csv", skiprows=19, usecols=np.r_[0:3])
Time = data.loc[:,'Time (s)'].to_list()
V_DUC = data.loc[:,'Channel 1 (V)'].to_list()
V_tot = data.loc[:,'Channel 2 (V)'].to_list()
x_rlim = max(T_time)
y_ulim = max(max(V_DUC), max(V_tot))
x_llim = min(V_tot)
y_dlim = min(V_DUC)

slope, intercept, r_value, p_value, std_err = stats.linregress(V_tot, V_DUC)
print('y = (%f) + (%f) * x' % (intercept, slope))
print('r^2 = %f' % r_value**2)
x = np.linspace(x_llim, x_rlim, 100)
y = intercept + slope * x


plt.title('')
plt.title('Correlation between $\mathrm{V_{tot}}$ and $\mathrm{V_{DUC}}$')
plt.xlabel('$\mathrm{V_{tot}}$[V]')
plt.ylabel('$\mathrm{V_{DUC}}$[mV]')
plt.xlim(x_llim, x_rlim)
plt.ylim(y_dlim, y_ulim)
plt.plot(V_tot, V_DUC, '.', label='experiment', markersize = 1, color = 'black')
plt.plot(x, y, label='fitted', color = 'blue', linewidth = 2)
plt.legend(loc=0)
#plt.show() 하면 pdf출력이 안됨. 왜그런지는 모르겠음
#plt.show()
plt.savefig(os.path.join(save_path,'1_ice_temperture_drop_the_bit(not_beat)'))