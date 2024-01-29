import streamlit as st


def page():
    st.title("나의 프로젝트 정보")

    if 'page1_selections' in st.session_state:
        st.subheader("페이지 1의 선택 내역")
        for selection in st.session_state['page1_selections']:
            st.write(selection)






