# file: fit_example2.py

import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats as ss

m = 100

data = pd.read_csv('Binomial-fichas.csv')
data = data.loc[:m,'GM']
print(f'data:\n{data}')

fitted_results = ss.fit(ss.binom,data,bounds=[(0,100),(0,1)])
print(fitted_results)
fitted_results.plot()
plt.show()