# file: fit.py

import numpy as np
import pandas as pd
from scipy import optimize as sco

x_exp = [1,2,3,4,5,6]
y_exp = [1,2,3,4,5,6]

x_exp = [i+(np.random.random()-0.5)*0.1 for i in x_exp]
y_exp = [i+(np.random.random()-0.5)*0.1 for i in x_exp]

# print(x_exp)

def recta(x,m,b):
    return m*x + b

fit, cov_mat = sco.curve_fit(recta,x_exp,y_exp)

m = fit[0]
b = fit[1]

print(f'Este es el valor de m: {m}\nEste es el valor de b: {b}')

