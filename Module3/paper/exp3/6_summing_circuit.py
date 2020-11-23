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

DC_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#DC_list = [8]

for DC in DC_list:
    save_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'figure')
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data\\exp3\\6_Module2sine_1kHz_OP97F_sine_0.5V_DC'+str(DC)+'00mV.csv')

    #data = dictionary format data from WaveForms exported raw data
    data = csv_data(data_path)
    X = [data['time'], data['time']]
    Y = [data['V1'], data['V2']]
    #print(min(data['V2']), max(data['V2']), np.average(data['V2']))
    #print(min(data['V1']), max(data['V1']), np.average(data['V1']))
    Plot(X, Y , X_unit = 's', Y_unit = 'V', X_name = '$t$', Y_name = '$V_{in}, V_{out}$', graph_name = 'exp3_6_summing_circuit_DC'+str(DC)+'00mV', save_path = save_path, linear_fit = False, File_format = 'jpg', labels = ('$V_{in}$','$V_{out}$'))
