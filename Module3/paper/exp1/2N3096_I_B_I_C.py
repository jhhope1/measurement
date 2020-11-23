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
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data\\exp1\\2N3906\\exp_I_B_I_C_sameasprev.csv')

#data = dictionary format data from WaveForms exported raw data
data = csv_data(data_path)
X = data['V1']/1e5
Y = data['V2']/100
Plot(X, Y , X_unit = 'A', Y_unit = 'A', X_name = '$I_{B}$', Y_name = '$I_{C}$', graph_name = '2N3906_IB_IC', save_path = save_path, linear_fit = True, File_format = 'jpg')
