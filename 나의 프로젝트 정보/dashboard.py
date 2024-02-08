import streamlit as st


def page():
    st.title("선택한 사항들 입니다")
    
    tab1, tab2, tab3 = st.tabs(["사용자 정보 입력", "주제 설정", "AI 구현 설계"])

    with tab1:
        ai_level = st.session_state.get('ai_level', '정보 없음')
        activity_field = st.session_state.get('activity_field', '정보 없음')
        selected_purposes_str = ', '.join(st.session_state.get('selected_purposes', ['목적 없음']))
        st.subheader(f"1. AI습득 정도 선택 : {ai_level}")
        st.subheader(f"2. 신분 선택 : {activity_field}")
        st.subheader(f"3. 목적 선택 : {selected_purposes_str}")

    with tab2:
        purpose1 = st.session_state.get('purpose1', '정보 없음')
        purpose2 = st.session_state.get('purpose2', '정보 없음')
        work_type = st.session_state.get('work_type', '정보 없음')
        work_order = st.session_state.get('work_order', '정보 없음')
        main_function = st.session_state.get('main_function', '정보 없음')
        ai_benefits = st.session_state.get('ai_benefits', '정보 없음')
        st.subheader(f"1: {purpose1}")
        st.subheader(f"2: {purpose2}")
        st.subheader(f"3: {work_type}")
        st.subheader(f"4: {work_order}")
        st.subheader(f"5: {main_function}")
        st.subheader(f"6: {ai_benefits}")

    with tab3:
        stp_1 = st.session_state.get('stp_1', '정보 없음')
        stp_2 = st.session_state.get('stp_2', '정보 없음')
        stp_3 = st.session_state.get('stp_3', '정보 없음')
        step_1_selection = st.session_state.get('step_1_selection', '정보 없음')
        step_1 = st.session_state.get('step_1', '정보 없음')
        step3 = st.session_state.get('step3', '정보 없음')
        step4 = st.session_state.get('step4', '정보 없음')
        st.header("STEP1")
        st.subheader(f"1단계 : {stp_1}")
        st.subheader(f"2단계: {stp_2}")
        st.subheader(f"3단계: {stp_3}")
        st.header("STEP2")
        #st.subheader(f"1단계(STEP1 선택): {step_1}")
        st.subheader(f"1단계(STEP1 선택): {step_1_selection}")
        st.subheader(f"2단계: {step3}")
        st.subheader(f"3단계: {step4}")