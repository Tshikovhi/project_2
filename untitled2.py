# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 00:47:20 2024

@author: lk
"""

import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd


data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 20, 15, 25]
})

st.title('Streamlit ECharts App')

chart_data = data.set_index('Category')

st_echarts(chart_data, height=400, theme="dark")