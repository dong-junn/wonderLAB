import streamlit as st
import pandas as pd


def page():
    # 세션 상태 초기화 함수

    st.title("AI 솔루션 도입 평가")

    st.subheader("AI 솔루션 도입으로 인한 업무 처리 시간의 변화 평가")

    # Initialize the DataFrame in session state if it doesn't exist
    if 'df' not in st.session_state:
        st.session_state.df = pd.DataFrame(columns=['도입 전(시간)', '도입 후(시간)'])

    col1, col2 = st.columns(2)

    with col1:
        # Directly use the key parameter without assigning to st.session_state
        input_before = st.text_input("도입 전", key='input_before')

    with col2:
        input_after = st.text_input("도입 후", key='input_after')

    # Button to reset the DataFrame and clear inputs
    if st.button("초기화"):
        st.session_state.df = pd.DataFrame(columns=['도입 전(시간)', '도입 후(시간)'])
        # Clear input fields by resetting them in the session state
        st.session_state.input_before = ''
        st.session_state.input_after = ''

    # Check if there are inputs before adding them to the DataFrame
    if input_before and input_after:
        # Instead of appending to the DataFrame, replace it with the new inputs
        st.session_state.df = pd.DataFrame({'도입 전(시간)': [input_before], '도입 후(시간)': [input_after]})

    st.write(st.session_state.df)

    # Streamlit의 session_state를 초기화합니다.
    if 'time_change' not in st.session_state:
        st.session_state['time_change'] = ''
    if 'cost_change' not in st.session_state:
        st.session_state['cost_change'] = '변화 없음'
    if 'cost_measurement' not in st.session_state:
        st.session_state['cost_measurement'] = '비용 대비 ROI 계산'
    if 'quality_impact' not in st.session_state:
        st.session_state['quality_impact'] = '변화 없음'
    if 'quality_measurement' not in st.session_state:
        st.session_state['quality_measurement'] = '고객 만족도'
    if 'staff_change' not in st.session_state:
        st.session_state['staff_change'] = '동일'
    if 'staff_management' not in st.session_state:
        st.session_state['staff_management'] = '재교육 및 재배치'
    if 'procedure_impact' not in st.session_state:
        st.session_state['procedure_impact'] = '변화 없음'
    if 'procedure_evaluation' not in st.session_state:
        st.session_state['procedure_evaluation'] = '처리 시간 단축'

    # 질문 1: AI 솔루션 도입 전후 각각의 업무에 소요되는 평균 시간
    st.subheader("1. AI 솔루션 도입 전후 각각의 업무에 소요되는 평균 시간")
    st.text_input("시간 변화 선택", key='time_change')

    # 질문 2: AI 솔루션 도입 전후의 업무 운영 비용 변화
    st.subheader("2. AI 솔루션 도입 전후의 업무 운영 비용 변화")
    st.selectbox("비용 변화 선택", ["상당히 절감", "약간 절감", "변화 없음", "증가"], key='cost_change')

    # 질문 3: AI 솔루션 도입에 따른 비용 절감 효과 측정
    st.subheader("3. AI 솔루션 도입에 따른 비용 절감 효과 측정")
    st.selectbox("비용 절감 효과 측정 방법 선택", ["비용 대비 ROI 계산", "업무 처리 시간 감소", "인력 비용 절감"], key='cost_measurement')

    # 질문 4: AI 솔루션 도입이 업무 결과물의 품질에 미치는 영향
    st.subheader("4. AI 솔루션 도입이 업무 결과물의 품질에 미치는 영향")
    st.selectbox("품질 영향 선택", ["상당히 향상", "약간 향상", "변화 없음", "저하"], key='quality_impact')

    # 질문 5: 업무 결과물의 품질 변화 측정 지표
    st.subheader("5. 업무 결과물의 품질 변화 측정 지표")
    st.selectbox("품질 변화 측정 지표 선택", ["고객 만족도", "오류율 감소", "처리 속도"], key='quality_measurement')

    # 질문 6: AI 도입 전후 업무에 필요한 인력 수 변화
    st.subheader("6. AI 도입 전후 업무에 필요한 인력 수 변화")
    st.selectbox("인력 수 변화 선택", ["감소", "동일", "증가"], key='staff_change')

    # 질문 7: AI 도입으로 인한 인력 구성의 변화 관리 및 계획
    st.subheader("7. AI 도입으로 인한 인력 구성의 변화 관리 및 계획")
    st.selectbox("인력 구성 변화 관리 방법 선택", ["재교육 및 재배치", "인력 축소", "전문 인력 채용"], key='staff_management')

    # 질문 8: AI 솔루션 도입이 업무 절차에 미치는 영향
    st.subheader("8. AI 솔루션 도입이 업무 절차에 미치는 영향")
    st.selectbox("업무 절차 변화 선택", ["상당히 간소화", "약간 간소화", "변화 없음", "복잡해짐"], key='procedure_impact')

    # 질문 9: 업무 절차의 간소화 평가 기준
    st.subheader("9. 업무 절차의 간소화 평가 기준")
    st.selectbox("절차 간소화 평가 기준 선택", ["처리 시간 단축", "오류율 감소", "사용자 만족도 증가"], key='procedure_evaluation')

    st.divider()

    # Displaying summaries of user inputs
    st.subheader(f"1: {st.session_state.get('time_change', '정보 없음')}")
    st.subheader(f"2: {st.session_state.get('cost_change', '정보 없음')}")
    st.subheader(f"3: {st.session_state.get('cost_measurement', '정보 없음')}")
    st.subheader(f"4: {st.session_state.get('quality_impact', '정보 없음')}")
    st.subheader(f"5: {st.session_state.get('quality_measurement', '정보 없음')}")
    st.subheader(f"6: {st.session_state.get('staff_change', '정보 없음')}")
    st.subheader(f"7: {st.session_state.get('staff_management', '정보 없음')}")
    st.subheader(f"8: {st.session_state.get('procedure_impact', '정보 없음')}")
    st.subheader(f"9: {st.session_state.get('procedure_evaluation', '정보 없음')}")
