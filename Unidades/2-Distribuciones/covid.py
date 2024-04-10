# file: covid.py

import pandas as pd
import numpy as np
from scipy import stats as sst
from matplotlib import pyplot as plt
import math

# conf_fecha = pd.read_csv('confirmados_fecha.csv',header=0,date_format='Y-m-d')
conf_fecha = pd.read_csv('confirmados_fecha.csv',header=0)
conf_fecha = conf_fecha.loc[0:50]
print(conf_fecha)

# print('\n',conf_fecha['date'][0])
# print(type(conf_fecha['date'][0]))

data = []

for row_i, row_data in conf_fecha.iterrows():
    # print('\n',row_i)
    # print(row_data)

    for i in range(row_data['sintomas']):
        data.append(row_data['index'])

print(data)

fitted_plot = sst.fit(sst.binom,data,[(0,400),(0,1)],guess=[400,0.9])
print(fitted_plot)
fitted_plot.plot()
plt.show()

def fit(x):
    A = 100
    u = 500
    r = 5
    return A*math.exp(-((x-u)/r)**2/2)

fig,axis = plt.subplots(1)

x_list = [1,2,3]
y_list = [fit(xi) for xi in x_list]

fig.lines(x_list,y_list)
