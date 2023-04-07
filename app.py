import streamlit as st
from multiapp import MultiApp
from apps import Dataset, Predictions, RefCode

app = MultiApp()

# Add all your application here
app.add_app("Dataset", Dataset.app)
app.add_app("Predictions", Predictions.app)
app.add_app("RefCode", RefCode.app)
app.run()
