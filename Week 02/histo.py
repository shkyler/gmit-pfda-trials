# 2018-09-30 Patrick Moore - GMIT - Programming for Data Analyis Week 02 - Testing the Matplotlob functionality from the lectures

#import matplotlib.pyplot (pyplot is the package from matplot lib that provides the plotting funcitonality)
import matplotlib.pyplot as plt 
import numpy as np 

x = np.random.normal(0.0, 1.0, 10000)
plt.subplot(1, 2, 1)
plt.axis([-5, 5, 0, 3500])
plt.hist(x)


y = np.random.uniform(-3.0, 3.0, 10000)
plt.subplot(2, 2, 2)
plt.axis([-5, 5, 0, 3500])
plt.hist(y)

z = np.random.uniform(-3.0, 3.0, 10000)
plt.subplot(2, 2, 4)
plt.axis([-5, 5, 0, 3500])
plt.hist(z)

plt.show()