# 2018-09-30 Patrick Moore - GMIT - Programming for Data Analyis Week 02 - Testing the Matplotlob functionality from the lectures

#import matplotlib.pyplot (pyplot is the package from matplot lib that provides the plotting funcitonality)
import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(-2.0 * np.pi, 2.0 * np.pi, 0.1)

plt.plot(x, np.sin(x), 'b.', label='sin(x)')
plt.plot(x, np.cos(x), 'r.', label='cos(x)')
plt.legend()

plt.show()