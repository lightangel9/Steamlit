import streamlit as st
from predictions
from dataset
from ref_code

# เมนูเปลี่ยนหน้า
menu = ['1_Predictions', '2_Dataset', '3_RefCode']
choice = st.sidebar.selectbox("เลือกหน้าเว็บ", menu)

# ตรวจสอบเลือกหน้าเว็บและแสดงเนื้อหาตามที่เลือก
if choice == '1_Predictions':
    1_predictions()
elif choice == '2_Dataset':
    2_dataset()
elif choice == '3_RefCode':
    3_ref_code)

