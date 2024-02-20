import os
import json
import streamlit as st
from streamlit_chat import message


def page():

    # JSON로드
    current_dir = os.path.dirname(os.path.abspath(__file__))

    data_path = os.path.join(current_dir, 'aiModeling.json')

    with open(data_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # session_state 초기화
    # step1
    for key in ['aiModeling_step1Checkbox1', 'aiModeling_step1Checkbox2', 'aiModeling_step1CheckboxNo1',
                'aiModeling_step1Checkbox3', 'aiModeling_step1CheckboxNo2',
                'aiModeling_step1Checkbox4', 'aiModeling_step1CheckboxNo3']:
        if key not in st.session_state:
            st.session_state[key] = False

    # step2
    for key in ['aiModeling_step2Checkbox1', 'aiModeling_step2Checkbox2', 'aiModeling_step2CheckboxNo']:
        if key not in st.session_state:
            st.session_state[key] = False

    # step3
    for key in ['aiModeling_step3Checkbox1', 'aiModeling_step3CheckboxNo1',
                'aiModeling_step3Checkbox2', 'aiModeling_step3CheckboxNo2']:
        if key not in st.session_state:
            st.session_state[key] = False

    # step4
    for key in ['aiModeling_step4Checkbox1', 'aiModeling_step4CheckboxNo']:
        if key not in st.session_state:
            st.session_state[key] = False

    # step1
    def step1Checkbox1():
        st.session_state.aiModeling_step1Checkbox1 = not st.session_state.aiModeling_step1Checkbox1
    def step1Checkbox2():
        st.session_state.aiModeling_step1Checkbox2 = not st.session_state.aiModeling_step1Checkbox2
    def step1CheckboxNo1():
        st.session_state.aiModeling_step1CheckboxNo1 = not st.session_state.aiModeling_step1CheckboxNo1
    st.subheader("단계 1: 데이터셋 업로드 절차")
    with st.expander("질문 1: 'AI wonder' 웹사이트에 접속하셨나요?"):

        st.checkbox(data["step1"]["checkbox1"], key="aiM_step1Checkbox1", value=st.session_state.aiModeling_step1Checkbox1, on_change=step1Checkbox1)
        st.checkbox(data["step1"]["checkbox2"], key="aiM_step1Checkbox2", value=st.session_state.aiModeling_step1Checkbox2, on_change=step1Checkbox2)

        step1Disable1 = st.session_state.aiModeling_step1Checkbox1 and st.session_state.aiModeling_step1Checkbox2
        st.checkbox(data["checkboxNo"], key="aiM_CheckboxNo1", value=st.session_state.aiModeling_step1CheckboxNo1, on_change=step1CheckboxNo1, disabled=step1Disable1)


    def step1Checkbox3():
        st.session_state.aiModeling_step1Checkbox3 = not st.session_state.aiModeling_step1Checkbox3

    def step1CheckboxNo2():
        st.session_state.aiModeling_step1CheckboxNo2 = not st.session_state.aiModeling_step1CheckboxNo2

    with st.expander("질문 2: '데이터 수집' 페이지에 접근하셨나요?"):
        st.checkbox(data["step1"]["checkbox3"], key="aiM_step1Checkbox3", value=st.session_state.aiModeling_step1Checkbox3, on_change=step1Checkbox3)

        step1Disable2 = st.session_state.aiModeling_step1Checkbox3
        st.checkbox(data["checkboxNo"], key="aiM_step1CheckboxNo2", value=st.session_state.aiModeling_step1CheckboxNo2, on_change=step1CheckboxNo2, disabled=step1Disable2)


    def step1Checkbox4():
        st.session_state.aiModeling_step1Checkbox4 = not st.session_state.aiModeling_step1Checkbox4
    def step1CheckboxNo3():
        st.session_state.aiModeling_step1CheckboxNo3 = not st.session_state.aiModeling_step1CheckboxNo3


    with st.expander("질문 3: 데이터셋 파일을 업로드하셨나요?"):
        st.checkbox(data["step1"]["checkbox4"], key="aiM_step1Checkbox4", value=st.session_state.aiModeling_step1Checkbox4, on_change=step1Checkbox4)

        step1Disable3 = st.session_state.aiModeling_step1Checkbox4
        st.checkbox(data["checkboxNo"], key="aiM_step1CheckboxNo3", value=st.session_state.aiModeling_step1CheckboxNo3, on_change=step1CheckboxNo3, disabled=step1Disable3)




    # step2
    def step2Checkbox1():
        st.session_state.aiModeling_step2Checkbox1 = not st.session_state.aiModeling_step2Checkbox1
    def step2Checkbox2():
        st.session_state.aiModeling_step2Checkbox2 = not st.session_state.aiModeling_step2Checkbox2
    def step2CheckboxNo():
        st.session_state.aiModeling_step2CheckboxNo = not st.session_state.aiModeling_step2CheckboxNo


    st.subheader("단계 2: 업로드된 데이터셋 확인")
    with st.expander("질문 4: 업로드된 데이터셋이 정상적으로 표시되는지 확인하셨나요?"):
        st.checkbox(data["step2"]["checkbox1"], key="aiM_step2Checkbox1", value=st.session_state.aiModeling_step2Checkbox1, on_change=step2Checkbox1)
        st.checkbox(data["step2"]["checkbox2"], key="aiM_step2Checkbox2", value=st.session_state.aiModeling_step2Checkbox2, on_change=step2Checkbox2)

        step2Disable1 = st.session_state.aiModeling_step2Checkbox1 and st.session_state.aiModeling_step2Checkbox2
        st.checkbox(data["checkboxNo"], key="aiM_step2CheckboxNo", value=st.session_state.aiModeling_step2CheckboxNo, on_change=step2CheckboxNo, disabled=step2Disable1)


    # step3
    def step3Checkbox1():
        st.session_state.aiModeling_step3Checkbox1 = not st.session_state.aiModeling_step3Checkbox1
    def step3CheckboxNo1():
        st.session_state.aiModeling_step3CheckboxNo1 = not st.session_state.aiModeling_step3CheckboxNo1
    def step3Checkbox2():
        st.session_state.aiModeling_step3Checkbox2 = not st.session_state.aiModeling_step3Checkbox2
    def step3CheckboxNo2():
        st.session_state.aiModeling_step3CheckboxNo2 = not st.session_state.aiModeling_step3CheckboxNo2

    st.subheader("단계 3: 데이터 분석 시작")
    with st.expander("질문 5: '데이터 분석' 버튼을 클릭하여 기본 분석을 시작하셨나요?"):
        st.checkbox(data["step3"]["checkbox1"], key="aiM_step3Checkbox1", value=st.session_state.aiModeling_step3Checkbox1, on_change=step3Checkbox1)

        step3Disable1 = st.session_state.aiModeling_step3CheckboxNo1
        st.checkbox(data["checkboxNo"], key="aiM_step3CheckboxNo1", value=st.session_state.aiModeling_step3CheckboxNo1, on_change=step3CheckboxNo1, disabled=step3Disable1)

    with st.expander("질문 6: 데이터 분석의 결과를 확인하셨나요?"):
        st.checkbox(data["step3"]["checkbox2"], key="aiM_step3Checkbox2", value=st.session_state.aiModeling_step3Checkbox2, on_change=step3Checkbox2)

        step3Disable2 = st.session_state.aiModeling_step3Checkbox2
        st.checkbox(data["checkboxNo"], key="aiM_step3CheckboxNo2", value=st.session_state.aiModeling_step3CheckboxNo2, on_change=step3CheckboxNo2, disabled=step3Disable2)


    def step4Checkbox1():
        st.session_state.aiModeling_step4Checkbox1 = not st.session_state.aiModeling_step4Checkbox1
    def step4CheckboxNo():
        st.session_state.aiModeling_step4CheckboxNo = not st.session_state.aiModeling_step4CheckboxNo


    # step4
    st.subheader("단계 4: Target 변수 지정")
    with st.expander("질문 7: 분석할 Target 변수를 선정하셨나요?"):
        st.checkbox(data["step4"]["checkbox1"], key="aiM_step4Checkbox1", value=st.session_state.aiModeling_step4Checkbox1, on_change=step4Checkbox1)

        step4Disable1 = st.session_state.aiModeling_step4CheckboxNo
        st.checkbox(data["checkboxNo"], key="aiM_step4CheckboxNo", value=st.session_state.aiModeling_step4CheckboxNo, on_change=step4CheckboxNo, disabled=step4Disable1)
    st.divider()







