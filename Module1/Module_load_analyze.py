import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt
from const import *
#load csv file to pandas dataframe
#You can use this scope when analyze data
Power_V_df = pd.read_csv(os.path.join(PARENT_PATH, 'tutorial_df.csv'))
Oscillo1 = Power_V_df['Oscillo1_list']
Oscillo2 = Power_V_df['Oscillo2_list']
Power_V = Power_V_df['Power_V_list']

I_list = Power_V/R_load

slope, intercept, r_value, _, std_err = stats.linregress(I_list, Oscillo1)
x = np.arange(len(I_list))
plt.plot(I_list, intercept + slope*I_list, 'r', label='fitted line')
plt.plot(I_list, Oscillo1, label = 'I_V curve')
plt.show()
print("slope = R_th = {:.5f}Ohm", slope)
print("R^2 = {:.5f}", r_value**2)