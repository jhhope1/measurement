import numpy as np
from matplotlib import pyplot as plt
x = np.arange(0, 1000, 0.01)
y = np.sin(x)
z = 0.7*np.cos(x)
alpha = 0.7
yp = y*np.cos(alpha)-z*np.sin(alpha)
zp = y*np.sin(alpha)+z*np.cos(alpha)
plt.plot(yp, zp*0.4)
plt.xlim(-1,1)
plt.ylim(-1,1)

plt.show()