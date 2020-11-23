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
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data\\exp2\\exp2.1\\Vin_VBE.csv')

#data = dictionary format data from WaveForms exported raw data
data = csv_data(data_path, [0, 3000])
X = [data['time'], data['time']]
Y = [data['V1'], data['V2']]
Plot(X, Y , X_unit = 's', Y_unit = 'V', X_name = '$t$', Y_name = '$V_{in}, V_{BE}$', graph_name = 'CEA_V_in_V_BE', save_path = save_path, linear_fit = False, File_format = 'jpg', labels = ('$V_{in}$','$V_{BE}$'))
