import streamlit as st
import pandas as pd
import os
import json


def page():
    # JSON로드
    current_dir = os.path.dirname(os.path.abspath(__file__))

    data_path = os.path.join(current_dir, 'efficiency_metric.json')

    with open(data_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    st.title("AI 솔루션 도입 평가")

    # Session State 초기화
    if 'df' not in st.session_state:
        st.session_state.df = pd.DataFrame({
            "분류": ["업무 처리시간", "처리 비용", "투입 인원"],
            "도입 전": ["", "", ""],
            "도입 후": ["", "", ""]
        }).set_index('분류')
    # UI 구성
    st.title("AI 솔루션 도입 효과 분석")

    # 1. 업무 처리 시간의 변화 평가
    st.subheader("1. AI 솔루션 도입으로 인한 업무 처리 시간의 변화 평가")
    col1, col2 = st.columns(2)
    with col1:
        input_before = st.text_input(data["step1"]["before"], key='input_before')
    with col2:
        input_after = st.text_input(data["step1"]["after"], key='input_after')
    # 2. 업무 운영 비용 변화
    st.subheader("2. AI 솔루션 도입 전후의 업무 운영 비용 변화")
    col1, col2 = st.columns(2)
    with col1:
        time_before = st.text_input(data["step2"]["before"], key='time_before')
    with col2:
        time_after = st.text_input(data["step2"]["after"], key='time_after')
    # 3. 비용 절감 효과 측정
    st.subheader("3. AI 솔루션 도입에 따른 비용 절감 효과 측정")
    col1, col2 = st.columns(2)
    with col1:
        cost_before = st.text_input(data["step3"]["before"], key='cost_before')
    with col2:
        cost_after = st.text_input(data["step3"]["after"], key='cost_after')
    # 데이터 추가 및 초기화 버튼
    if st.button("입력"):
        st.session_state.df.at["업무 처리시간", "도입 전"] = input_before
        st.session_state.df.at["업무 처리시간", "도입 후"] = input_after
        st.session_state.df.at["처리 비용", "도입 전"] = time_before
        st.session_state.df.at["처리 비용", "도입 후"] = time_after
        st.session_state.df.at["투입 인원", "도입 전"] = cost_before
        st.session_state.df.at["투입 인원", "도입 후"] = cost_after
        st.success("데이터가 추가되었습니다.")
    if st.button("초기화"):
        st.session_state.df = pd.DataFrame({
            "분류": ["업무 처리시간", "처리 비용", "투입 인원"],
            "도입 전": ["", "", ""],
            "도입 후": ["", "", ""]
        }).set_index('분류')
        st.success("데이터가 초기화되었습니다.")

    st.dataframe(st.session_state.df, use_container_width=True)
    # 질문 4: AI 솔루션 도입이 업무 결과물의 품질에 미치는 영향
    st.subheader("4. AI 솔루션 도입이 업무 결과물의 품질에 미치는 영향")
    def update_quality_impact(new_value):
        st.session_state['quality_impact'] = new_value
    st.session_state['quality_impact'] = st.selectbox(
        data["step4"]["selectbox_label"],
        data["step4"]["option"],
        index=data["step4"]["option"].index(st.session_state['quality_impact']),
        on_change=update_quality_impact,
        args=(st.session_state['quality_impact'],)
    )
    # 질문 5: 업무 결과물의 품질 변화 측정 지표
    st.subheader("5. 업무 결과물의 품질 변화 측정 지표")
    def update_quality_measurement(new_value):
        st.session_state['quality_measurement'] = new_value
    st.session_state['quality_measurement'] = st.selectbox(
        data["step5"]["selectbox_label"],
        data["step5"]["option"],
        index=data["step5"]["option"].index(st.session_state['quality_measurement']),
        on_change=update_quality_measurement,
        args=(st.session_state['quality_measurement'],)
    )
    # 질문 6: AI 도입 전후 업무에 필요한 인력 수 변화
    st.subheader("6. AI 도입 전후 업무에 필요한 인력 수 변화")
    def update_staff_change(new_value):
        st.session_state['staff_change'] = new_value
    st.session_state['staff_change'] = st.selectbox(
        data["step6"]["selectbox_label"],
        data["step6"]["option"],
        index=data["step6"]["option"].index(st.session_state['staff_change']),
        on_change=update_staff_change,
        args=(st.session_state['staff_change'],)
    )
    # 질문 7: AI 도입으로 인한 인력 구성의 변화 관리 및 계획
    st.subheader("7. AI 도입으로 인한 인력 구성의 변화 관리 및 계획")
    def update_staff_management(new_value):
        st.session_state['staff_management'] = new_value

    st.session_state['staff_management'] = st.selectbox(
        "인력 구성 변화 관리 방법 선택",
        ["재교육 및 재배치", "인력 축소", "전문 인력 채용"],
        index=["재교육 및 재배치", "인력 축소", "전문 인력 채용"].index(st.session_state['staff_management']),
        on_change=update_staff_management,
        args=(st.session_state['staff_management'],)
    )
    # 질문 8: AI 솔루션 도입이 업무 절차에 미치는 영향
    st.subheader("8. AI 솔루션 도입이 업무 절차에 미치는 영향")
    def update_procedure_impact(new_value):
        st.session_state['procedure_impact'] = new_value
    st.session_state['procedure_impact'] = st.selectbox(
        "업무 절차 변화 선택",
        ["상당히 간소화", "약간 간소화", "변화 없음", "복잡해짐"],
        index=["상당히 간소화", "약간 간소화", "변화 없음", "복잡해짐"].index(st.session_state['procedure_impact']),
        on_change=update_procedure_impact,
        args=(st.session_state['procedure_impact'],)
    )
    # 질문 9: 업무 절차의 간소화 평가 기준
    st.subheader("9. 업무 절차의 간소화 평가 기준")
    def update_procedure_evaluation(new_value):
        st.session_state['procedure_evaluation'] = new_value
    st.session_state['procedure_evaluation'] = st.selectbox(
        "절차 간소화 평가 기준 선택",
        ["처리 시간 단축", "오류율 감소", "사용자 만족도 증가"],
        index=["처리 시간 단축", "오류율 감소", "사용자 만족도 증가"].index(st.session_state['procedure_evaluation']),
        on_change=update_procedure_evaluation,
        args=(st.session_state['procedure_evaluation'],)
    )
    st.divider()

    # Displaying summaries of user inputs
    # st.subheader(f": {st.session_state.time_change}")
    # st.subheader(f": {st.session_state.time_change}")
    #st.subheader(f": {st.session_state.time_change}")
    # st.subheader(f"5: {st.session_state.quality_impact}")
    # st.subheader(f"6: {st.session_state.quality_measurement}")
    # st.subheader(f"7: {st.session_state.staff_change}")
    # st.subheader(f"8: {st.session_state.staff_management}")
    # st.subheader(f"9: {st.session_state.procedure_impact}")
    # st.subheader(f"10: {st.session_state.procedure_evaluation}")
    #st.subheader(f": {st.session_state.}")
    #st.subheader(f": {st.session_state.}")
