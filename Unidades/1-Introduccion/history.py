 1/1: %history -o -g -f ipython_history.py
 1/3: %history -o -g -f ipython_history.py
17/14: clear
 2/1: 3!
 2/2: clear
 2/3: import math
 2/4: math.comb(3)
 2/5: math.comb(3,3)
 2/6: math.comb(3,2)
 2/7: math.comb(4,2)
 2/8: clear
 2/9: math.comb(1000,33)
2/10: clear
 3/1: clear
 3/2: import streamlit as st
 4/1: clear
 4/2: import pandas as pd
 5/1: clear
 5/2: import numpy as np
 5/3: import random as rnd
 5/4: rnd.gauss(15,10)
 5/5: rnd.gauss(15,1)
 5/6: rnd.gauss(15,5)
 5/7: rnd.gauss(15,5)
 5/8: rnd.gauss(15,5)
 5/9: rnd.gauss(15,5)
5/10: rnd.gauss(15,5)
5/11: rnd.gauss(15,5)
5/12: rnd.gauss(15,2)
5/13: rnd.gauss(15,2)
5/14: rnd.gauss(15,2)
5/15: rnd.gauss(15,2)
5/16: clear
5/17: for i in range(5)
5/18:
for i in range(5):
    l.append(rnd.gauss(15,2))
5/19: l = []
5/20:
for i in range(5):
    l.append(rnd.gauss(15,2))
5/21: l
 6/1: clear
 6/2: f = lambda x,y: x+y
 6/3: f(1,2)
 7/1: import scipy as sp
 7/2: sp.optimize.curve_fit()
 7/3: a = [1,2,3,4,5]
 7/4: b = a
 7/5:
def f(x,a,b):
    return ax+b
 7/6: la = a
 7/7: lb = b
 7/8: sp.optimize.curve_fit(f,la,lb)
 7/9:
def f(x,a,b):
    return a*x+b
7/10: sp.optimize.curve_fit(f,la,lb)
7/11: sa = [1,0.9,1.1,0.9]
7/12: sp.optimize.curve_fit(f,la,lb,sigma=sa)
7/13: a
7/14: sa = [1,0.9,1.1,0.9,0.8]
7/15: sp.optimize.curve_fit(f,la,lb,sigma=sa)
7/16: sp.optimize.curve_fit(f,la,lb)
7/17: sp.optimize.curve_fit(f,la,lb,sigma=sa)
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
