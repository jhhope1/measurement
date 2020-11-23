import pandas as pd
import numpy as np
import csv

#return numpy array of V1, V2, time as a python dictionary
def csv_data(data_path, rangelr = None):
    f = open(data_path, 'r')
    rdr = csv.reader(f)
    for idx, line in enumerate(rdr):
        line = str(line)
        if line[:6]=='[\'Time':
            break
        else:
            l = 1
            print(line)
    f.close()
    data = pd.read_csv(data_path, skiprows=idx)
    time = np.array(list(data['Time (s)']))
    V1 = np.array(list(data['Channel 1 (V)']))
    V2 = np.array(list(data['Channel 2 (V)']))
    if rangelr!=None:
        time = time[rangelr[0]:rangelr[1]]
        V1 = V1[rangelr[0]:rangelr[1]]
        V2 = V2[rangelr[0]:rangelr[1]]
    return {'time': time, 'V1': V1, 'V2': V2}