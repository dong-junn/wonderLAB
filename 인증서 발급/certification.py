import streamlit as st
from PIL import Image


def page():

    # 인증서 발급
    st.subheader("인증서 발급")

    st.markdown("""
    - 평가 기준에 부합하는 참여자에게는 인증서가 발급됩니다.
    - 인증서에는 참여자의 이름, 프로젝트의 성격, 평가 기준 충족 여부 등이 명시됩니다.
    """)

    st.subheader("인증서 예시")
    example_certificate = Image.open("association_certification.png")
    st.image(example_certificate)

    # 인증서의 활용
    st.subheader("인증서의 활용")

    st.markdown("""
    - 인증서는 참여자가 다양한 상황에서 인공지능을 효과적으로 적용할 수 있는 능력을 갖추었음을 증명하는 중요한 문서입니다.
    - 이는 참여자의 이력서, 학술 논문, 프로젝트 제안서 등에 포함되어 전문성과 신뢰성을 높일 수 있습니다.
    """)