import streamlit as st
from PIL import Image

def page():
    st.title("AI 솔루션 도입 평가")

    # 1번 질문
    st.subheader("AI 솔루션 도입 전후 각각의 업무에 소요되는 평균 시간")
    time_change = st.selectbox("시간 변화 선택", ["30% 감소", "동일", "증가"], key='1')

    # 2번 질문
    st.subheader("AI 솔루션 도입으로 인한 업무 처리 시간의 변화 평가")
    time_evaluation = st.selectbox("시간 변화 평가 선택", ["매우 효율적", "일부 효율적", "변화 없음", "비효율적"], key='2')

    # 3번 질문
    st.subheader("AI 솔루션 도입 전후의 업무 운영 비용 변화")
    cost_change = st.selectbox("비용 변화 선택", ["상당히 절감", "약간 절감", "변화 없음", "증가"], key='3')

    # 4번 질문
    st.subheader("AI 솔루션 도입에 따른 비용 절감 효과 측정")
    cost_measurement = st.selectbox("비용 절감 효과 측정 방법 선택", ["비용 대비 ROI 계산", "업무 처리 시간 감소", "인력 비용 절감"], key='4')

    # 5번 질문
    st.subheader("AI 솔루션 도입이 업무 결과물의 품질에 미치는 영향")
    quality_impact = st.selectbox("품질 영향 선택", ["상당히 향상", "약간 향상", "변화 없음", "저하"], key='5')

    # 6번 질문
    st.subheader("업무 결과물의 품질 변화 측정 지표")
    quality_measurement = st.selectbox("품질 변화 측정 지표 선택", ["고객 만족도", "오류율 감소", "처리 속도"], key='6')

    # 7번 질문
    st.subheader("AI 도입 전후 업무에 필요한 인력 수 변화")
    staff_change = st.selectbox("인력 수 변화 선택", ["감소", "동일", "증가"], key='7')

    # 8번 질문
    st.subheader("AI 도입으로 인한 인력 구성의 변화 관리 및 계획")
    staff_management = st.selectbox("인력 구성 변화 관리 방법 선택", ["재교육 및 재배치", "인력 축소", "전문 인력 채용"], key='8')

    # 9번 질문
    st.subheader("AI 솔루션 도입이 업무 절차에 미치는 영향")
    procedure_impact = st.selectbox("업무 절차 변화 선택", ["상당히 간소화", "약간 간소화", "변화 없음", "복잡해짐"], key='9')

    # 10번 질문
    st.subheader("업무 절차의 간소화 평가 기준")
    procedure_evaluation = st.selectbox("절차 간소화 평가 기준 선택", ["처리 시간 단축", "오류율 감소", "사용자 만족도 증가"], key='10')