import os
import sys
import numpy as np
import pandas as pd

#Include your library path in sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

#Include your Library
from graph_library.pltgraph import Plot
from graph_library.csvreader import csv_data

#save_path = save figure
#data_path = csv file path

R_list = [1, 2.5, 2, 3, 5]
R_list = [2.5]

for R in R_list:
    save_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'figure')
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data\\exp3\\7_Module2sine_1kHz_OP97F_sine_1V_1kOhm_'+str(R)+'kOhm.csv')

    #data = dictionary format data from WaveForms exported raw data
    data = csv_data(data_path)
    X = [data['time'], data['time']]
    Y = [data['V1'], data['V2']]
    
    print(min(data['V2']), max(data['V2']), np.average(data['V2']))
    print(min(data['V1']), max(data['V1']), np.average(data['V1']))
    Plot(X, Y , X_unit = 's', Y_unit = 'V', X_name = '$t$', Y_name = '$V_{in}, V_{out}$', graph_name = 'exp3_7_non_inverting_'+str(R)+'kOhm', save_path = save_path, linear_fit = False, File_format = 'jpg', labels = ('$V_{in}$','$V_{out}$'))
