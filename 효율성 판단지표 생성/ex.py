import streamlit as st
from PIL import Image

def page():
    st.title("효율성 판단지표 생성")

    op_1 = st.number_input(
        "소요시간 입력(키보드로 입력도 가능)",
        min_value=1,
        max_value=100
    )

    op_2 = st.number_input(
        "인력 수 입력(키보드로 입력도 가능)",
        min_value=1,
        max_value=100
    )

    op_3 = st.text_input("월 급여 입력")

    st.write("소요시간: ", str(op_1))
    st.write("인력 수 : ", str(op_2))
    st.write("월 급여: ", op_3)

    tem1 = Image.open("images/efficiency_1.jpg")
    st.image(tem1)

    tem2 = Image.open("images/efficiency_2.jpg")
    st.image(tem2)