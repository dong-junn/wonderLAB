import streamlit as st

def project_intro():
    st.header("프로젝트 소개")
    # 드롭다운에 표시할 옵션 리스트
    options = ['사회', '경제', '과학','기타(직접작성)']

    # 드롭다운 생성
    selected_option = st.selectbox('대주제를 선택해주세요:', options)
    if selected_option == '기타(직접작성)':
        st.text_input('대주제를 적어주세요')

    st.text_area('개요 및 미션')
    st.text_area('목표 및 필요성')
    st.text_area('자격요건 및 신청')

    st.button('제출')