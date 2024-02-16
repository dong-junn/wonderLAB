import streamlit as st


def page():
    st.title("선택한 사항들 입니다")
    
    tab1, tab2, tab3, tab4 = st.tabs(["프로젝트 신청하기", "주제 설정", "AI 구현 설계", "효율성 판단지표"])

    with tab1:
        st.subheader(f"1. AI습득 정도 선택 : {st.session_state.ai_level}")
        st.subheader(f"2. 신분 선택 : {st.session_state.activity_field}")
        st.subheader(f"3. 목적 선택 : {st.session_state.selected_purposes_str}")

    with tab2:
        st.subheader(f"1: {st.session_state.purpose1}")
        st.subheader(f"2: {st.session_state.purpose2}")
        st.subheader(f"3: {st.session_state.work_typ}")
        st.subheader(f"4: {st.session_state.task_order}")
        st.subheader(f"5: {st.session_state.core_function}")
        st.subheader(f"6: {st.session_state.ai_advantages}")

    with tab3:
        stp_1 = st.session_state.get('stp_1', '아직 미입력하셨습니다')
        stp_2 = st.session_state.get('stp_2', '아직 미입력하셨습니다')
        stp_3 = st.session_state.get('stp_3', '아직 미입력하셨습니다')
        step_1_selection = st.session_state.get('step_1_selection', '아직 미입력하셨습니다')
        step_1 = st.session_state.get('step_1', '아직 미입력하셨습니다')
        step3 = st.session_state.get('step3', '아직 미입력하셨습니다')
        step4 = st.session_state.get('step4', '아직 미입력하셨습니다')
        st.header("STEP1")
        st.subheader(f"1단계 : {stp_1}")
        st.subheader(f"2단계: {stp_2}")
        st.subheader(f"3단계: {stp_3}")
        st.header("STEP2")
        #st.subheader(f"1단계(STEP1 선택): {step_1}")
        st.subheader(f"1단계(STEP1 선택): {step_1_selection}")
        st.subheader(f"2단계: {step3}")
        st.subheader(f"3단계: {step4}")

    with tab4:
        st.subheader(f"AI 솔루션 도입이 업무 결과물의 품질에 미치는 영향: {st.session_state.quality_impact}")
        st.subheader(f"업무 결과물의 품질 변화 측정 지표: {st.session_state.quality_measurement}")
        st.subheader(f"AI 도입 전후 업무에 필요한 인력 수 변화: {st.session_state.staff_change}")
        st.subheader(f"AI 도입으로 인한 인력 구성의 변화 관리 및 계획: {st.session_state.staff_management}")
        st.subheader(f"AI 솔루션 도입이 업무 절차에 미치는 영향: {st.session_state.procedure_impact}")
        st.subheader(f"업무 절차의 간소화 평가 기준: {st.session_state.procedure_evaluation}")