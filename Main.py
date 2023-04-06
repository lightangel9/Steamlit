import streamlit as st

def main_page():
    st.markdown("Main page 🎈")
    st.sidebar.markdown("Main page 🎈")

def page1():
    st.markdown("1_🐶_Predictions")
    st.sidebar.markdown("1_🐶_Predictions")

def page2():
    st.markdown("2_📊_Dataset")
    st.sidebar.markdown("2_📊_Dataset")
   
def page3():
    st.markdown("3_👨‍💻_RefCode")
    st.sidebar.markdown("3_👨‍💻_RefCode")


page_names_to_funcs = {
    "Main Page": main_page,
    "Page 1": page1,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
