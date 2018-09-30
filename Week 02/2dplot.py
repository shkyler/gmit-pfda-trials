# 2018-09-30 Patrick Moore - GMIT - Programming for Data Analyis Week 02 - Testing the Matplotlob functionality from the lectures

#import matplotlib.pyplot (pyplot is the package from matplot lib that provides the plotting funcitonality)
import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(0.0, 10.0, 0.01) 
y = 3.0 * x + 1.0
noise = np.random.normal(0.0, 1.0, len(x)) 

plt.plot(x, y + noise, 'r.', label="Data")
plt.plot(x, y, 'b-', label="Linear")

plt.title("Weight vs. Moisture")
plt.xlabel("Moisture")
plt.ylabel("Weight")
plt.legend()

plt.show()


