# file: fit_example.py

import numpy as np
import pandas as pd
from scipy import optimize as sco
from scipy import special as ssp
import math
import plotly.express as px

m = 100

def binom(x,n,p):
    print('binom(',x,n,p,')')
    
    # x = int(x)
    # n = int(n)
        
    comb = ssp.comb(n,x)
    p_x = p**x
    q_nx = (1-p)**(n-x)

    return comb*p_x*q_nx
    # return A * scs.binom.pmf(x,n,p)

# binom = np.vectorize(binom)


data = pd.read_csv('Binomial-fichas.csv')
print(f'data:\n{data}')

data = data.loc[:m]

counts_non_sort = data['GM'].value_counts()
counts = pd.DataFrame(np.zeros(11))
# print(counts)

for row, value in counts_non_sort.items():
    counts.loc[row,0] = value

print(f'counts:\n{counts}')
print(f'index: {counts.index.values}')
print(f'normalized counts: {list(counts[0]/m)}')


fit, cov_mat = sco.curve_fit(binom,counts.index.values,counts[0]/m,bounds=[(0,0),(np.inf,1)])

print(f'Fit:\n{fit}\ncov_mat\n{cov_mat}')

n = fit[0]
p = fit[1]

print(f'Este es el valor de n: {n}\nEste es el valor de p: {p}')




binomial_plot = px.line(x=counts.index.values, y=binom(counts.index.values,n,p), title="Lanzamiento de fichas")

binomial_plot.add_bar(x=counts.index.values, y=counts[0]/m, name='Lanzamientos experimentales')

binomial_plot.show()

