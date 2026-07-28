import streamlit as st
import pandas as pd

st.title('Machine Learning Project 1')

st.write('This app is built to use machine learning to predict the housing value in California using machine learning!')

with st.expander( 'Data'):
  st.write('**Raw Data**')
  df = pd.read_csv(...)
  df

  st.write('**X**')
  X = df.drop('Metal', axis=1)
