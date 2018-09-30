# 2018-09-30 Patrick Moore - GMIT - Programming for Data Analyis Week 02 - Testing the Matplotlob functionality from the lectures

#import matplotlib.pyplot (pyplot is the package from matplot lib that provides the plotting funcitonality)
import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(0.1, 10.0, 0.1)
y = np.arange(0.1, 15.0, 0.1)
z = np.arange(0.1, 20.0, 0.1)
c = np.arange(0.1, 25.0, 0.1)

plt.subplot(2,2,1)
plt.plot(x, x**2, 'b.', label='x^2')
plt.plot(x, x**3, 'r.', label='x^3')
plt.plot(x, x**4, 'g.', label='x^4')
plt.plot(x, 2**x, 'y.', label='2^x')
plt.legend()

plt.subplot(2,2,2)
plt.plot(y, y**2, 'b.', label='x^2')
plt.plot(y, y**3, 'r.', label='x^3')
plt.plot(y, y**4, 'g.', label='x^4')
plt.plot(y, 2**y, 'y.', label='2^x')
plt.legend()

plt.subplot(2,2,3)
plt.plot(z, z**2, 'b.', label='x^2')
plt.plot(z, z**3, 'r.', label='x^3')
plt.plot(z, z**4, 'g.', label='x^4')
plt.plot(z, 2**z, 'y.', label='2^x')
plt.legend()

plt.subplot(2,2,4)
plt.plot(c, c**2, 'b.', label='x^2')
plt.plot(c, c**3, 'r.', label='x^3')
plt.plot(c, c**4, 'g.', label='x^4')
plt.plot(c, 2**c, 'y.', label='2^x')
plt.legend()

plt.show()