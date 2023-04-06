import streamlit as st
from pages import page_1_predictions, page_2_dataset, page_3_ref_code

# เมนูเปลี่ยนหน้า
menu = ['1_Predictions', '2_📊_Dataset', '3_👨‍💻_RefCode.py']
choice = st.sidebar.selectbox("เลือกหน้าเว็บ", menu)

# ตรวจสอบเลือกหน้าเว็บและแสดงเนื้อหาตามที่เลือก
if choice == '1_Predictions':
    page_1_predictions.show()
elif choice == '2_Dataset':
    page_2_dataset.show()
elif choice == '3__RefCode.py':
    page_3_ref_code.show()

