import streamlit as st

# สร้างหน้าเว็บแรกที่ชื่อว่า "1_Predictions"
def page_1_predictions():
    st.title('1_Predictions')
    # เพิ่มเนื้อหาหน้าเว็บ 1_Predictions

# สร้างหน้าเว็บที่สองที่ชื่อว่า "2_📊_Dataset"
def page_2_dataset():
    st.title('2_📊_Dataset')
    # เพิ่มเนื้อหาหน้าเว็บ 2_📊_Dataset

# สร้างหน้าเว็บที่สามที่ชื่อว่า "3_👨‍💻_RefCode.py"
def page_3_ref_code():
    st.title('3_👨‍💻_RefCode.py')
    # เพิ่มเนื้อหาหน้าเว็บ 3_👨‍💻_RefCode.py

# สร้างเมนูเพื่อเปลี่ยนหน้าเว็บ
def create_sidebar_menu():
    # ใช้ st.sidebar.selectbox เพื่อสร้างเมนูเลือกหน้าเว็บ
    selected_page = st.sidebar.selectbox('เลือกหน้าเว็บ', ('1_Predictions', '2_📊_Dataset', '3_👨‍💻_RefCode.py'))

    # ใช้เงื่อนไข (conditional statements) เพื่อแสดงหน้าเว็บที่ถูกเลือก
    if selected_page == '1_Predictions':
        page_1_predictions()
    elif selected_page == '2_📊_Dataset':
        page_2_dataset()
    elif selected_page == '3_👨‍💻_RefCode.py':
        page_3_ref_code()

# เรียกใช้ฟังก์ชันสำหรับสร้างเมนูเปลี่ยนหน้าเว็บ
create_sidebar_menu()
