import streamlit as st
import Dataset

def main():
    menu = ["Predictions", "Dataset"]
    choice = st.sidebar.radio("ไปที่", menu)

    if choice == "Predictions":
        st.subheader('📊Dataset')
        st.success('**Original dataset from Kaggle.com 🌐**')
        st.markdown('🔗URL: https://www.kaggle.com/datasets/jessicali9530/stanford-dogs-dataset')
        st.subheader('Context')
        st.text('Stanford Dogs dataset contains images of 120 breeds of dogs from around the world.')
        st.subheader('Content')
        st.text('Number of categories: 120')
        st.text('Number of images: 20,580')
        st.text('Annotations: Class labels, Bounding boxes')
    elif choice == "Dataset":
        Dataset.app()

if __name__ == '__main__':
    main()
