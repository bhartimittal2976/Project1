import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl','rb') as file:
        data = pickle.load(file)
    return data

    data = load_model()

    regressor_loaded = data["model"]

    def show_predict_page():
        st.title("Prediction of Annual Income")

        st.write("""### We need some information to predict the annual income""")


    

