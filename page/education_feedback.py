import streamlit as st

def education_feedback():
    st.header("교육후기")

    st.text_area('프로그램 교육후기에 대해서 적어주세요')

    st.button('제출')


