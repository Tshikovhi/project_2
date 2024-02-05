# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 23:41:49 2024

@author: lk
"""

pip install streamlit
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as
pip install streamlit
data = pd.read_csv("iris.csv")
st.title('Iris Dataset Exploration')
st.write('Sample of the data:')
st.write(data.head())
st.write('Basic Statistics:')
st.write(data.describe())
st.write('Pair Plot:')
sns.pairplot(data, hue='class')
st.pyplot()