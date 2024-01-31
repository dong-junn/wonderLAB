import streamlit as st
import pandas as pd


def page():
    st.subheader("평가의 중요성 및 목적")
    st.markdown("""
    - 평가는 참가자들이 프로젝트를 통해 얻은 인공지능 관련 지식과 기술을 실제 상황에 어떻게 적용할 수 있는지를 평가하는 데 목적이 있습니다.
    - 평가 과정은 참가자들에게 자신들의 프로젝트와 인공지능 활용에 대한 깊은 통찰력을 제공하며, 실제 문제 해결에 AI를 적용하는 방법에 대한 이해를 증진시킵니다.
    """)


    st.subheader("평가 방법 및 핵심 요소")
    st.markdown("""
    - **문제 인식 및 적용 능력**: 참가자들이 식별한 문제의 실질성과 그 문제에 인공지능을 적용하는 능력을 평가합니다.
    - **업무 효율성 개선**: 인공지능 적용으로 인한 구체적인 업무 효율성 개선 사항을 평가합니다.
    - **혁신성 및 창의성**: 인공지능 적용이 기존 업무 방식에 비해 얼마나 혁신적이고 창의적인 해결책을 제공하는지를 측정합니다.
    """)


    st.subheader("평가 결과의 활용")
    st.markdown("""
    - 평가 결과는 참가자들에게 인공지능 기술을 실무에 통합하고 실제 문제를 해결하는 데 필요한 능력을 개발했는지를 보여줍니다.
    - 평가 결과는 평가자들이 각 참가자의 프로젝트에 대해 피드백을 제공하고, 참가자들이 향후 개선할 수 있는 영역을 지적하는 데 사용됩니다.
    """)


    st.subheader("인증서 발급 기준")
    st.markdown("""
    - 인증서는 참가자들이 평가 기준에 부합하는 능력을 보여주었을 때 수여됩니다.
    - 인증서 발급은 참가자들이 이 프로그램을 통해 얻은 경험과 성취를 공식적으로 인정하고, 그들의 전문성을 강조하는 수단으로 활용됩니다.
    """)


    st.subheader("평가 제출")
    st.text_input("참가자 이름")
    st.file_uploader("제출하기", type=['pdf', 'docx'])
    st.button("제출")




    '''
    st.subheader("문제 발굴 및 AI를 문제 해결 도구로 적용(25점)")
    st.subheader(
        "수많은 생활, 업무, 연구, 학교학습에서 어떤 문제를 인공지능의 핵심기능으로 해결할 수 있는지 발굴 하였나요?")

    select = st.selectbox(
        "항목별로 선택해주세요",
        ('주제', '기존 업무', '연구', '생활', '학교 학습 과정', '데이터 작성 가능 단계', '시뮬레이션 과정')
    )

    if select == '주제':
        st.text_input("주제를 입력해주세요")

    elif select == '기존 업무':
        st.text_input("기존 업무가 무엇이였나요?")

    elif select == '연구':
        st.text_input("어떠한 연구를 했는지 입력해주세요")

    elif select == '생활':
        st.text_input("어떠한 생활을 했는지 입력해주세요")

    elif select == '학교 학습 과정':
        st.text_input("학교 학습 과정은 무엇인가요?")

    elif select == '시뮬레이션 과정':
        st.text_input("시뮬레이션 과정을 자세히 입력해주세요")

    # 2

    st.subheader("인공지능 기능 적용능력(25점)")
    st.subheader("인공지능의 핵심 기능(분류, 예측, 클러스터링) 중에서 어떤 기능을 어떤 데이터를 기반으로 이해하였나요?")
    st.selectbox(
        "선택해주세요",
        ('분류', '예측', '클러스터링')
    )

    st.subheader("업무방식 개선 (25점)")
    st.subheader("인공지능을 문제 해결 도구로 활용하는 방식을 비교하는 테이블을 작성해주세요")
    st.text_input("기존방식")
    st.text_input("인공지능 적용 방식")


    # 2열 10행의 빈 데이터프레임 생성
    df = pd.DataFrame({"기존방식": [""] * 10, "인공지능 적용 방식": [""] * 10})

    # Streamlit 앱에서 st.dataframe을 사용하여 데이터프레임 출력
    st.dataframe(df)

    
    st.subheader("업무방식 개선(25점)")
    st.subheader("최종 구현된 인공지능 모델과 AI wonder의 Test 부분의 입력과 결과값을 화면캡쳐해서 올려주세요")
    st.file_uploader("화면 업로드", type="img, jpg, jpeg, png", accept_multiple_files=True)

    mark_style = """
    <style>
        #f990558c {
            margin-bottom: 30px;   
        }
        
        #81919f41 {
            margin-bottom: 0px;
        }
    </style>
    """

    st.markdown(mark_style, unsafe_allow_html=True)'''
