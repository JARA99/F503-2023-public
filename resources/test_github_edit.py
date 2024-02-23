# file: test_github_edit.py

import streamlit as st
import pandas as pd

st.title('Titulo 1')

data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')

st.table(data)

st.markdown('## Texto:\n
hola mundo')

