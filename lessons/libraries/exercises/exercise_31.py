from math import pi

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate, special

x_values = np.arange(0,pi/2,0.00001)
y_values = [np.sin(i) for i in x_values]

#Integral de Riemann
riemann_integral = 0
for i in range(0, x_values.size-1):
    if(y_values[i]>y_values[i+1]):
        y = y_values[i+1]
    else:
        y = y_values[i]
    riemann_integral += (x_values[i+1]-x_values[i])*y

#SciPy
scipy_integral = 0
scipy_integral_tuple = integrate.quad(lambda x : np.sin(x),0,pi/2)
scipy_integral = scipy_integral_tuple[0]

plt.plot(x_values,y_values,'.-',color="red",label="sin function")

plt.title("Sin function")
plt.legend()
plt.grid(True)
