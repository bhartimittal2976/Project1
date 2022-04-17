import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from autoviz.AutoViz_Class import AutoViz_Class
AV = AutoViz_Class()

def load_data():
    df = pd.read_csv("Ecommerce.csv")
@st.cache
filename = "Ecommerce.csv"
sep = ","
dft = AV.AutoViz(
    filename,
    sep=",",
    depVar="",
    dfte=None,
    header=0,
    verbose=0,
    lowess=False,
    chart_format="html",
    max_rows_analyzed=150000,
    max_cols_analyzed=30,
)
df = load_data()

def show_explorer():
    st.title("Explore Predicted Annual Income")

    st.write(
        """
    ### Annual Income Prediction for Ecommerce Sector
    """
    )
