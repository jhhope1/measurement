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
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data\\exp1\\2N3904\\exp_0.6_1.6_.._4.6_tri_0_5V_100kOhm_100Ohm_IB_VCE.csv')

#data = dictionary format data from WaveForms exported raw data
data = csv_data(data_path)
X = data['V1']+0.6
Y = data['V2']/100
Plot(X, Y , X_unit = 'V', Y_unit = 'A', X_name = '$V_{CE}$', Y_name = '$I_{C}$', graph_name = '2N3904_IC_VCE', save_path = save_path, linear_fit = False, File_format = 'jpg')
