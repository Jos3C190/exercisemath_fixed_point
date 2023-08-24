#José Carlos López Martínez

import math
import numpy as np
import matplotlib.pyplot as plt

def original_function(x):
    return np.vectorize(math.exp)(-x)  

def iteration_function(x):
    return np.vectorize(math.exp)(-x)  

initial_estimation = 0.5
tolerance = 1e-4  
max_iterations = 1000 

fixed_point = initial_estimation
iterations = 0

while iterations < max_iterations:
    new_fixed_point = iteration_function(fixed_point)
    error = abs(new_fixed_point - fixed_point)
    
    if error < tolerance:
        print("Punto fijo encontrado:", new_fixed_point, "después de", iterations, "iteraciones.")
        break
    
    fixed_point = new_fixed_point
    iterations += 1
else:
    print("No se encontró el punto fijo después de las iteraciones máximas.")


# Grafica
range_values = np.linspace(0, 1, 1000)
fx = original_function(range_values)
gx = iteration_function(range_values)

plt.plot(range_values, fx, label='f(x)')
plt.plot(range_values, gx, label='g(x)')
plt.plot(range_values, range_values, label='y=x')

if 'new_fixed_point' in locals():
    plt.axvline(new_fixed_point, color='r', linestyle='--', label='Fixed Point')

plt.axhline(0, color='k')
plt.title('Fixed Point')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
