import os
import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#Include your library path in sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

#Include your Library
from graph_library.pltgraph import Plot
from graph_library.csvreader import csv_data

#save_path = save figure
#data_path = csv file path
save_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'figure')
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data\\exp1\\ZVN2110A\\NMOS_VDS_vs_ID_stair_offset_1.7.csv')

#data = dictionary format data from WaveForms exported raw data
data = csv_data(data_path, [0, 4000])
V_tot = data['V1']+data['V2']
X = np.array([data['time'], data['time']])
Y = np.array([data['V1'], data['V2']])
Plot(X, Y , X_unit = 's', Y_unit = 'V', X_name = '$t$', Y_name = '$V_{DS}, I_{D}R_{1}$', graph_name = 'ZVN2110A_I_D_V_DS_Offset_1.7', save_path = save_path, linear_fit = False, File_format = 'jpg', labels = ['$V_{DS}$', '$I_{D}R_{1}$'])

plt.show()