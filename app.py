import streamlit as st
from multiapp import MultiApp
from Pages import Predictions, Dataset, RefCode

app = MultiApp()

# Add all your application here
app.add_app("Predictions", Predictions.app)
app.add_app("Dataset", Dataset.app)
app.add_app("RefCode", RefCode.app)

