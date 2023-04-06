import streamlit as st

# เมนูเปลี่ยนหน้า
menu = ['1_Predictions', '2_📊_Dataset', '3_👨‍💻_RefCode.py']
choice = st.sidebar.selectbox("เลือกหน้าเว็บ", menu)

# ฟังก์ชันสำหรับแสดงเนื้อหาในหน้าเว็บ 1_Predictions
def page_1_predictions():
    st.title('1_Predictions')
    # เพิ่มเนื้อหาหรือโค้ดที่ต้องการแสดงผลในหน้าเว็บ 1_Predictions ตรงนี้

# ฟังก์ชันสำหรับแสดงเนื้อหาในหน้าเว็บ 2_📊_Dataset
def page_2_dataset():
    st.title('2_📊_Dataset')
    # เพิ่มเนื้อหาหรือโค้ดที่ต้องการแสดงผลในหน้าเว็บ 2_📊_Dataset ตรงนี้

# ฟังก์ชันสำหรับแสดงเนื้อหาในหน้าเว็บ 3_👨‍💻_RefCode.py
def page_3_ref_code():
    st.title('3_👨‍💻_RefCode.py')
    # เพิ่มเนื้อหาหรือโค้ดที่ต้องการแสดงผลในหน้าเว็บ 3_👨‍💻_RefCode.py ตรงนี้

# ตรวจสอบเลือกหน้าเว็บและแสดงเนื้อหาตามที่เลือก
if choice == '1_Predictions':
    page_1_predictions()
elif choice == '2_📊_Dataset':
    page_2_dataset()
elif choice == '3_👨‍💻_RefCode.py':
    page_3_ref_code()
