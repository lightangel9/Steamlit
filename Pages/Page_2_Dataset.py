import streamlit as st

# สร้างหน้าเว็บที่สอง
def page_2_dataset():
    st.title('2_Dataset')
    # เพิ่มเนื้อหาหน้าเว็บ 2_📊_Dataset

# เรียกใช้ฟังก์ชันสำหรับสร้างหน้าเว็บ 2_📊_Dataset
page_2_dataset()

    st.subheader('📊Dataset')
    st.success('**Original dataset from Kaggle.com 🌐**')
    st.markdown('🔗URL: https://www.kaggle.com/datasets/jessicali9530/stanford-dogs-dataset')
    st.subheader('Context')
    st.text('Stanford Dogs dataset contains images of 120 breeds of dogs from around the world.')
    st.subheader('Content')
    st.text('Number of categories: 120')
    st.text('Number of images: 20,580')
    st.text('Annotations: Class labels, Bounding boxes')
