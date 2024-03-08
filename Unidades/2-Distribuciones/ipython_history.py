   1: clear
   2: import pandas as pd
   3: import numpy as np
   4: np.empty((4,20))
   5: np.empty((20,4))
   6: np.empty((20,3))
   7: a = np.empty((20,3))
   8: a
   9: clear
  10: np.empty((20,3))
  11: a
  12: clear
  13: a = np.zeros((20,3))
  14: a
  15: a = np.empty((20,3))
  16: a
  17: clear
  18: a = np.random((20,3))
  19: a = np.random.rand((20,3))
  20: a = np.random.random((20,3))
  21: clear
  22: a
  23: a_pandas = pd.DataFrame(a)
  24: a_pandas
  25: a_pandas.columns = ['a','b','c']
  26: a_pandas
  27: a_pandas['a']
  28: a_pandas['a'][3:7]
  29: a_pandas['a'][7]
  30: a_pandas['a'][:7]
  31: a_pandas['a'][:]
  32: a_pandas[:][:7]
  33: a_pandas[['b','a']][:7]
  34: %history -o -g -f ipython_history.py
  35: %history -o -g -f ./history.py
  36: a_pandas['a']
  37: list(a_pandas['a'])
  38: a_pandas['a'].to_list()
  39: np.array(a_pandas['a'])
  40: a_pandas['a'].to_numpy()
  41: clear
  42: tup = (1,2,3)
  43: a,b,c = tup
  44: a
  45: b
  46: c
  47: (a,b,c) = tup
  48: a
  49: [1,2,5,3,9,0,-1]
  50: a = [1,2,5,3,9,0,-1]
  51: a.sort()
  52: a
  53: a = [1,2,5,3,9,0,-1,2,5,2,9,0,9,2,0,9,2,2,9]
  54: np.array(a)
  55: a_np = np.array(a)
  56: a_np
  57: a_pd = pd.DataFrame(a)
  58: a_pd
  59: a_pd.count
  60: a_pd.count(2)
  61: a_pd.count()
  62: a_pd.count(axis=1)
  63: a_pd.groupby(axis=1)
  64: a_pd.value_counts()
  65: a_pd.value_counts()[2]
  66: a_pd.value_counts()[-1]
  67: %history -o -g -f ./history.py
