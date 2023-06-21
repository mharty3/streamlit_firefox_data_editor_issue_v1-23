import streamlit as st
import pandas as pd

st.title("Data frame and data editor v1.22.0")

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

"## Dataframe v1.22.0"
"""With v1.22.0, I can click and drag to select multiple cells to copy from the dataframe.

I can use keyboard shortcuts like shift + arrow keys to navigate around the dataframe and select cells.
"""
st.dataframe(df)

"## Data editor v1.22.0"
"""With the experimental data editor in v1.22.0, 
I can paste multiple cells into the dataframe. 

I can also use the "bulk edit" handle (or Ctrl+D/R) to fill in multiple cells at once. """
st.experimental_data_editor(df)

