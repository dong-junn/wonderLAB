import streamlit as st
from PIL import Image

def page():
    tem1 = Image.open("images/AI구현설계_1.png")
    st.image(tem1)


    """
    st.title("프로젝트 진행")

    st.subheader("STEP1: 기존 업무 단계를 입력해주세요")

    stp_1 = st.text_input("1단계 (예제 : 특정정보 수집)")
    stp_2 = st.text_input("2단계 (예제 : 키워드 기반으로 고객 반응 분석)")
    stp_3 = st.text_input("3단계 (예제 : 보고서 작성)")

    st.write("1단계 입력: ", stp_1)
    st.write("2단계 입력: ", stp_2)
    st.write("3단계 입력: ", stp_3)

    st.subheader("STEP2: 데이터수집 부분은 어디인가요?")
    step_1 =st.selectbox(
        "1단계 (STEP1 입력사항 선택)",
        (stp_1, stp_2, stp_3)
    )

    step3_1 = "분류(개/고양이 구분)"
    step3_2 = "예측(3일, 35명 등등 숫자로 예측)"
    step3_3 = "클러스터링 (군집화로 구분)"
    step3 = st.selectbox(
        "2단계 (수집된 데이터에 적용할 수 있는 AI기능은 무엇인가요?)",
        (step3_1, step3_2, step3_3)
    )

    step4_1 = "기본 업무 단계 시각화"
    step4_2 = "적용한 업무 단계 시각화"
    step4 = st.selectbox(
        "3단계 (기존 업무 단계를 인공지능을 적용하면 어떻게 변화시킬 수 있을까요? 다시 작성해주세요)",
        (step4_1, step4_2)
    )

    st.write("1단계 입력: ", step_1)
    st.write("2단계 입력: ", step3)
    st.write("3단계 입력: ", step4)
    """
    

