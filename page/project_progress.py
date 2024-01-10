import streamlit as st

def project_progress():
    st.header("프로젝트 진행")

    st.text_area('실행 계획안 작성')
    st.text_area('팀 등록 및 주제설정')
    st.text_area('프로젝트 가설 수립')
    st.text_area('기술 도구 선정')
    st.text_area('기술 구형 방법')

    st.button('제출')

    st.write('feedback')