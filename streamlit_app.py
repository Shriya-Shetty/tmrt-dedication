import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title('🎈 Tmrt Model Learning')

st.info("This is a analysis of the dedication of tmrt members")

with st.expander('TMRT DATA'):
  st.write('**DATA TABLE**')
  df = pd.read_csv('https://github.com/Shriya-Shetty/Model_Data/blob/efb7989b424d56fbfba763b46f1a62a5f0c129e9/Tmrt_hours.csv')
  df

