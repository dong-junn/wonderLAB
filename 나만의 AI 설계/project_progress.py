import streamlit as st
from PIL import Image


def page():
    st.title("프로젝트 진행")

    # STEP1: Initialize session state variables for the project steps if they don't exist
    for step in ['stp_1', 'stp_2', 'stp_3']:
        if step not in st.session_state:
            st.session_state[step] = ""

    st.subheader("STEP1: 기존 업무 단계를 입력해주세요")

    # Use session state variables for text inputs
    st.session_state.stp_1 = st.text_input("1단계 (예제 : 특정정보 수집)", value=st.session_state.stp_1)
    st.session_state.stp_2 = st.text_input("2단계 (예제 : 키워드 기반으로 고객 반응 분석)", value=st.session_state.stp_2)
    st.session_state.stp_3 = st.text_input("3단계 (예제 : 보고서 작성)", value=st.session_state.stp_3)

    st.title("")

    # STEP2
    st.subheader("STEP2: 데이터수집 부분은 어디인가요?")

    # Initialize session state variables for STEP2 selections if they don't exist
    if 'step_1_selection' not in st.session_state:
        st.session_state['step_1_selection'] = st.session_state.stp_1

    # 예시를 위한 st.session_state 초기화 코드 (실제 사용 시 필요한 곳에 적절히 배치)
    if 'stp_1' not in st.session_state:
        st.session_state['stp_1'] = "예제 입력 1"
    if 'stp_2' not in st.session_state:
        st.session_state['stp_2'] = "예제 입력 2"
    if 'stp_3' not in st.session_state:
        st.session_state['stp_3'] = "예제 입력 3"
    if 'step_1_selection' not in st.session_state:
        st.session_state['step_1_selection'] = st.session_state['stp_1']  # 초기 선택값 설정



    options = (st.session_state.stp_1, st.session_state.stp_2, st.session_state.stp_3)

    # step_1_selection 값이 옵션 목록에 있는지 확인하고, 없으면 기본값(예: 첫 번째 옵션)을 사용
    if st.session_state.step_1_selection not in options:
        default_index = 0  # 기본 인덱스 설정
    else:
        default_index = options.index(st.session_state.step_1_selection)

    step_1 = st.selectbox(
        "1단계 (STEP1 입력사항 선택)",
        options,
        index=default_index
    )

    # 선택된 값을 세션 상태에 업데이트
    st.session_state.step_1_selection = step_1

    step3_1 = "분류(개/고양이 구분)"
    step3_2 = "예측(3일, 35명 등등 숫자로 예측)"
    step3_3 = "클러스터링 (군집화로 구분)"
    st.session_state.step3 = st.selectbox(
        "2단계 (수집된 데이터에 적용할 수 있는 AI기능은 무엇인가요?)",
        (step3_1, step3_2, step3_3),
        index=(step3_1, step3_2, step3_3).index(st.session_state.step3)
    )

    step4_1 = "기본 업무 단계 시각화"
    step4_2 = "적용한 업무 단계 시각화"
    st.session_state.step4 = st.selectbox(
        "3단계 (기존 업무 단계를 인공지능을 적용하면 어떻게 변화시킬 수 있을까요? 다시 작성해주세요)",
        (step4_1, step4_2),
        index=(step4_1, step4_2).index(st.session_state.step4)
    )

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.header("STEP1")
        st.subheader(f"1단계: {st.session_state.stp_1}")
        st.subheader(f"2단계: {st.session_state.stp_2}")
        st.subheader(f"3단계: {st.session_state.stp_3}")

    with col2:
        st.header("STEP2")
        st.subheader(f"1단계: {st.session_state.step_1_selection}")
        st.subheader(f"2단계: {st.session_state.step3}")
        st.subheader(f"3단계: {st.session_state.step4}")
