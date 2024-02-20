import os
import json
import streamlit as st
from streamlit_chat import message


def page():

    # session_state초기화
    # step1
    for key in ['step1Checkbox1_q1', 'step1Checkbox2_q1', 'step1Checkbox3_q1', 'step1CheckboxNo_q1',
                'step1Checkbox1_q2', 'step1Checkbox2_q2', 'step1Checkbox3_q2', 'step1CheckboxNo_q2']:
        if key not in st.session_state:
            st.session_state[key] = False

    # step2 초기화
    for key in ['step2Checkbox1', 'step2Checkbox2', 'step2Checkbox3', 'step2Checkbox4', 'step2CheckboxNo']:
        if key not in st.session_state:
            st.session_state[key] = False

    # step3 초기화
    for key in ['step3Checkbox1', 'step3CheckboxNo']:
        if key not in st.session_state:
            st.session_state[key] = False

    # step4 초기화
    for key in ['step4Checkbox1', 'step4Checkbox2', 'step4CheckboxNo']:
        if key not in st.session_state:
            st.session_state[key] = False

    # step5 초기화
    for key in ['step5Checkbox1', 'step5Checkbox2', 'step5CheckboxNo']:
        if key not in st.session_state:
            st.session_state[key] = False

    # step6 초기화
    for key in ['step6Checkbox1', 'step6Checkbox2', 'step6CheckboxNo']:
        if key not in st.session_state:
            st.session_state[key] = False

    # step7 초기화
    for key in ['step7Checkbox1', 'step7CheckboxNo']:
        if key not in st.session_state:
            st.session_state[key] = False

    # JSON로드
    current_dir = os.path.dirname(os.path.abspath(__file__))

    data_path = os.path.join(current_dir, 'aiSimulation.json')

    with open(data_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # step1
    st.subheader("단계 1: 데이터셋 업로드 및 분석")
    with st.expander("질문 1: 'AI wonder'에서 데이터셋을 업로드하셨나요?"):
        def onChange_step1Checkbox1_q1():
            st.session_state.step1Checkbox1_q1 = not st.session_state.step1Checkbox1_q1

        def onChange_step1Checkbox2_q1():
            st.session_state.step1Checkbox2_q1 = not st.session_state.step1Checkbox2_q1

        def onChange_step1Checkbox3_q1():
            st.session_state.step1Checkbox3_q1 = not st.session_state.step1Checkbox3_q1

        def onChange_step1CheckboxNo_q1():
            st.session_state.onChange_step1CheckboxNo_q1 = not st.session_state.onChange_step1CheckboxNo_q1

        st.checkbox(data["step1"]["aiSimulation_step1Checkbox1_q1"], key="aiSimulation_step1Checkbox1_q1", value=st.session_state.step1Checkbox1_q1, on_change=onChange_step1Checkbox1_q1)
        st.checkbox(data["step1"]["aiSimulation_step1Checkbox2_q1"], key="aiSimulation_step1Checkbox2_q1", value=st.session_state.step1Checkbox2_q1, on_change=onChange_step1Checkbox2_q1)
        st.checkbox(data["step1"]["aiSimulation_step1Checkbox3_q1"], key="aiSimulation_step1Checkbox3_q1", value=st.session_state.step1Checkbox3_q1, on_change=onChange_step1Checkbox3_q1)

        step1_selectAll_q1 = st.session_state.step1Checkbox1_q1 and st.session_state.step1Checkbox2_q1 and st.session_state.step1Checkbox3_q1
        st.checkbox(data["checkboxNo"], key="aiSimulation_step1CheckboxNo_q1", value=st.session_state.step1CheckboxNo_q1, on_change=onChange_step1CheckboxNo_q1, disabled=step1_selectAll_q1)

    with st.expander("질문 2: 데이터셋에 대한 분석을 수행하셨나요?"):
        def onChange_step1Checkbox1_q2():
            st.session_state.step1Checkbox1_q2 = not st.session_state.step1Checkbox1_q2

        def onChange_step1Checkbox2_q2():
            st.session_state.step1Checkbox2_q2 = not st.session_state.step1Checkbox2_q2

        def onChange_step1Checkbox3_q2():
            st.session_state.step1Checkbox3_q2 = not st.session_state.step1Checkbox3_q2

        def onChange_step1CheckboxNo_q2():
            st.session_state.step1CheckboxNo_q2 = not st.session_state.step1CheckboxNo_q2

        st.checkbox(data["step1"]["aiSimulation_step1Checkbox1_q2"], key="aiSimulation_step1Checkbox1_q2", value=st.session_state.step1Checkbox1_q2, on_change=onChange_step1Checkbox1_q2)
        st.checkbox(data["step1"]["aiSimulation_step1Checkbox2_q2"], key="aiSimulation_step1Checkbox2_q2", value=st.session_state.step1Checkbox2_q2, on_change=onChange_step1Checkbox2_q2)
        st.checkbox(data["step1"]["aiSimulation_step1Checkbox3_q2"], key="aiSimulation_step1Checkbox3_q2", value=st.session_state.step1Checkbox3_q2, on_change=onChange_step1Checkbox3_q2)

        step1_selectAll_q2 = st.session_state.step1Checkbox1_q2 and st.session_state.step1Checkbox2_q2 and st.session_state.step1Checkbox3_q2
        st.checkbox(data["checkboxNo"], key="aiSimulation_step1CheckboxNo_q2", value=st.session_state.step1CheckboxNo_q2, on_change=onChange_step1CheckboxNo_q2, disabled=step1_selectAll_q2)

    # step2
    st.subheader("단계 2: 모델 빌딩 및 평가")
    with st.expander("질문 3: 타겟 변수를 예측하는 모델을 만들기 위한 준비를 하셨나요?"):
        def onChange_step2Checkbox1():
            st.session_state.step2Checkbox1 = not st.session_state.step2Checkbox1

        def onChange_step2Checkbox2():
            st.session_state.step2Checkbox2 = not st.session_state.step2Checkbox2

        def onChange_step2Checkbox3():
            st.session_state.step2Checkbox3 = not st.session_state.step2Checkbox3

        def onChange_step2Checkbox4():
            st.session_state.step2Checkbox4 = not st.session_state.step2Checkbox4

        def onChange_step2CheckboxNo():
            st.session_state.step2CheckboxNo = not st.session_state.step2CheckboxNo

        st.checkbox(data["step2"]["aiSimulation_step2Checkbox1"], key="aiSimulation_step2Checkbox1", value=st.session_state.step2Checkbox1, on_change=onChange_step2Checkbox1)
        st.checkbox(data["step2"]["aiSimulation_step2Checkbox2"], key="aiSimulation_step2Checkbox2", value=st.session_state.step2Checkbox2, on_change=onChange_step2Checkbox2)
        st.checkbox(data["step2"]["aiSimulation_step2Checkbox3"], key="aiSimulation_step2Checkbox3", value=st.session_state.step2Checkbox3, on_change=onChange_step2Checkbox3)
        st.checkbox(data["step2"]["aiSimulation_step2Checkbox4"], key="aiSimulation_step2Checkbox4", value=st.session_state.step2Checkbox4, on_change=onChange_step2Checkbox4)

        step2_selectAll = st.session_state.step2Checkbox1 and st.session_state.step2Checkbox2 and st.session_state.step2Checkbox3 and st.session_state.step2Checkbox4
        st.checkbox(data["checkboxNo"], key="aiSimulation_step2CheckboxNo", value=st.session_state.step2CheckboxNo, on_change=onChange_step2CheckboxNo, disabled=step2_selectAll)

    # step3
    st.subheader("단계 3: 모델 테스트 페이지 접근")
    with st.expander("질문 4: '모델 테스트' 페이지에 접근하셨나요?"):
        def onChange_step3Checkbox1():
            st.session_state.step3Checkbox1 = not st.session_state.step3Checkbox1

        def onChange_step3CheckboxNo():
            st.session_state.step3CheckboxNo = not st.session_state.step3CheckboxNo

        st.checkbox(data["step3"]["aiSimulation_step3Checkbox1"], key="aiSimulation_step3Checkbox1", value=st.session_state.step3Checkbox1, on_change=onChange_step3Checkbox1)
        st.checkbox(data["checkboxNo"], key="aiSimulation_step3CheckboxNo", value=st.session_state.step3CheckboxNo, on_change=onChange_step3CheckboxNo, disabled=st.session_state.step3Checkbox1)

    # step4
    st.subheader("단계 4: 예측 방식 선택")
    with st.expander("질문 5: 예측을 위한 방식을 선택하셨나요?"):
        def onChange_step4Checkbox1():
            st.session_state.step4Checkbox1 = not st.session_state.step4Checkbox1

        def onChange_step4Checkbox2():
            st.session_state.step4Checkbox2 = not st.session_state.step4Checkbox2

        def onChange_step4CheckboxNo():
            st.session_state.step4CheckboxNo = not st.session_state.step4CheckboxNo

        st.checkbox(data["step4"]["aiSimulation_step4Checkbox1"], key="aiSimulation_step4Checkbox1", value=st.session_state.step4Checkbox1, on_change=onChange_step4Checkbox1)
        st.checkbox(data["step4"]["aiSimulation_step4Checkbox2"], key="aiSimulation_step4Checkbox2", value=st.session_state.step4Checkbox2, on_change=onChange_step4Checkbox2)

        step4_selectAll = st.session_state.step4Checkbox1 and st.session_state.step4Checkbox2
        st.checkbox(data["checkboxNo"], key="aiSimulation_step4CheckboxNo", value=st.session_state.step4CheckboxNo, on_change=onChange_step4CheckboxNo, disabled=step4_selectAll)

    # step5
    st.subheader("단계 5: 입력값 준비 및 입력")
    with st.expander("질문 6: 가상의 웹앱에 필요한 입력값을 준비하셨나요?"):
        def onChange_step5Checkbox1():
            st.session_state.step5Checkbox1 = not st.session_state.step5Checkbox1

        def onChange_step5Checkbox2():
            st.session_state.step5Checkbox2 = not st.session_state.step5Checkbox2

        def onChange_step5CheckboxNo():
            st.session_state.step5CheckboxNo = not st.session_state.step5CheckboxNo

        st.checkbox(data["step5"]["aiSimulation_step5Checkbox1"], key="aiSimulation_step5Checkbox1", value=st.session_state.step5Checkbox1, on_change=onChange_step5Checkbox1)
        st.checkbox(data["step5"]["aiSimulation_step5Checkbox2"], key="aiSimulation_step5Checkbox2", value=st.session_state.step5Checkbox2, on_change=onChange_step5Checkbox2)

        step5_selectAll = st.session_state.step5Checkbox1 and st.session_state.step5Checkbox2
        st.checkbox(data["checkboxNo"], key="aiSimulation_step5CheckboxNo", value=st.session_state.step5CheckboxNo, on_change=onChange_step5CheckboxNo, disabled=step5_selectAll)

    # step6
    st.subheader("단계 6: 모델 예측 수행")
    with st.expander("질문 7: 모델을 테스트하여 예측을 수행하셨나요?"):
        def onChange_step6Checkbox1():
            st.session_state.step6Checkbox1 = not st.session_state.step6Checkbox1

        def onChange_step6Checkbox2():
            st.session_state.step6Checkbox2 = not st.session_state.step6Checkbox2

        def onChange_step6CheckboxNo():
            st.session_state.step6CheckboxNo = not st.session_state.step6CheckboxNo

        st.checkbox(data["step6"]["aiSimulation_step6Checkbox1"], key="aiSimulation_step6Checkbox1", value=st.session_state.step6Checkbox1, on_change=onChange_step6Checkbox1)
        st.checkbox(data["step6"]["aiSimulation_step6Checkbox2"], key="aiSimulation_step6Checkbox2", value=st.session_state.step6Checkbox2, on_change=onChange_step6Checkbox2)

        step6_selectAll = st.session_state.step6Checkbox1 and st.session_state.step6Checkbox2
        st.checkbox(data["checkboxNo"], key="aiSimulation_step6CheckboxNo", value=st.session_state.step6CheckboxNo, on_change=onChange_step6CheckboxNo, disabled=step6_selectAll)

    # step7
    st.subheader("단계 7: 테스트 결과 저장")
    with st.expander("질문 8: 테스트 결과를 저장하셨나요?"):
        def onChange_step7Checkbox1():
            st.session_state.step7Checkbox1 = not st.session_state.step7Checkbox1

        def onChange_step7CheckboxNo():
            st.session_state.step7CheckboxNo = not st.session_state.step7CheckboxNo

        st.checkbox(data["step7"]["aiSimulation_step7Checkbox1"], key="aiSimulation_step7Checkbox1", value=st.session_state.step7Checkbox1, on_change=onChange_step7Checkbox1)
        st.checkbox(data["checkboxNo"], key="aiSimulation_step7CheckboxNo", value=st.session_state.step7CheckboxNo, on_change=onChange_step7CheckboxNo, disabled=st.session_state.step7Checkbox1)

    st.divider()




