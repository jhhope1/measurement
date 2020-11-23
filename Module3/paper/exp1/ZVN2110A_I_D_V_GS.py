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
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data\\exp1\\ZVN2110A\\NMOS_ID_vs_VGS_XY_plot_100Ohm.csv')

#data = dictionary format data from WaveForms exported raw data
data = csv_data(data_path)
X = data['V1']
Y = data['V2']/100
Plot(X, Y , X_unit = 'V', Y_unit = 'A', X_name = '$V_{GS}$', Y_name = '$I_{D}$', graph_name = 'ZVN2110A_I_D_V_GS', save_path = save_path, linear_fit = False, File_format = 'jpg')
