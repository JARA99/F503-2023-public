# doc: ejercicio1.py

# imports
import numpy as np

# lista
ts = [3.3,3.2,3.0,3.4,2.9,3.5,3.3,3.4,3.2]

# promedio
t_mean = np.mean(ts)

# Desviación estandard (standard deviation)
t_std = np.std(ts)

# Distancia
d_mean = 7.0
d_std = 0.5

# Imprimir valores
print(f't_mean: {round(t_mean,1)}\nt_std: {round(t_std,1)}\nd_mean: {round(d_mean,1)}\nd_std: {round(d_std,1)}')

# Calcular v y v_pm
v_mean = d_mean/t_mean
v_pm_prob = ((1/t_mean)*d_std)-((d_mean/t_mean**2)*t_std)

print(f'v_mean: {round(v_mean,2)} ± {round(v_pm_prob,2)}')

# A pie
vs = []

for t in ts:
    v_temp = d_mean/t
    vs.append(v_temp)

print(vs)

# Con numpy
ts = np.array(ts)
print(ts)
vs_numpy = d_mean/ts
print(vs_numpy)

v_mean = vs_numpy.mean()
print(v_mean)
v_mean = np.mean(vs)
print(v_mean)

v_std = vs_numpy.std()
print(v_std)
v_std = np.std(vs,ddof=1)
print(v_std)



