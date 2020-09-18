import sys
import os
import numpy as np
PARENT_PATH = os.path.dirname(__file__)
#Module 1
SLEEP_TIME=0.01
SAMPLES=100
R_load = 5e3
Power_Max = 0.25
R_th = 110
V_max = min(np.sqrt((R_load+R_th)**2/R_th*Power_Max), 5)


#wheatstone
V_wheatstone = 5