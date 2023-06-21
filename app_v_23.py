import streamlit as st
import pandas as pd

st.title("Data frame and data editor v1.23.0")

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

"## Dataframe v1.23.0"
"""In v1.23.0, I can no longer select multiple cells at once with click and drag or keyboard shortcuts."""
st.dataframe(df)

"## Data editor v1.23.0"
"""In v1.23.0, I can no longer paste multiple cells into the dataframe. 
Nor can I use the "bulk edit" handle (or Ctrl+D/R) to fill in multiple cells at once."""
st.data_editor(df)
