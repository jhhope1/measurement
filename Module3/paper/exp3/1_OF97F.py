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
save_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'figure')
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data\\exp3\\1_Module2sine_2kHz_OP97F.csv')

#data = dictionary format data from WaveForms exported raw data
data = csv_data(data_path, [0, 2000])
X = [data['time'], data['time']]
Y = [data['V1'], data['V2']]
Plot(X, Y , X_unit = 's', Y_unit = 'V', X_name = '$t$', Y_name = '$V_{in}, V_{out}$', graph_name = 'exp3_1_OP97F', save_path = save_path, linear_fit = False, File_format = 'jpg', labels = ('$V_{in}$','$V_{out}$'))
