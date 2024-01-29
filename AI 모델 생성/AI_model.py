import streamlit as st


def page():

    # 1. 데이터셋 업로드 절차
    st.subheader("1. 데이터셋 업로드 절차")

    st.markdown("질문 1: 'AI wonder' 웹사이트에 접속하셨나요?")
    st.checkbox("예, 구글 크롬을 사용하여 www.ai-wonder.com에 접속했습니다.")
    st.checkbox("예, 페이지를 한국어로 번역했습니다.")

    st.markdown("질문 2: '데이터 수집' 페이지에 접근하셨나요?")
    st.checkbox("예, 'AI wonder' 메인 페이지에서 '데이터 수집' 섹션을 찾아 클릭했습니다.")

    st.markdown("질문 3: 데이터셋 파일을 업로드하셨나요?")
    st.checkbox("예, '파일찾아보기' 버튼을 클릭하여 엑셀 또는 .csv 파일을 선택하고 업로드했습니다.")

    # 2. 업로드된 데이터셋 확인
    st.subheader("2. 업로드된 데이터셋 확인")

    st.markdown("질문 4: 업로드된 데이터셋이 정상적으로 표시되는지 확인하셨나요?")
    st.checkbox("예, 페이지 하단으로 스크롤하여 업로드된 데이터셋을 확인했습니다.")
    st.checkbox("예, 모든 필요한 열과 데이터가 올바르게 나타나는지 검토했습니다.")

    # 3. 데이터 분석 시작
    st.subheader("3. 데이터 분석 시작")

    st.markdown("질문 5: '데이터 분석' 버튼을 클릭하여 기본 분석을 시작하셨나요?")
    st.checkbox("예, '데이터 분석' 버튼을 클릭하여 데이터셋에 대한 기본 분석을 수행했습니다.")

    st.markdown("질문 6: 데이터 분석의 결과를 확인하셨나요?")
    st.checkbox("예, 데이터의 개요 및 패턴을 이해하기 위해 분석 결과를 확인했습니다.")

    # 4. Target 변수 지정
    st.subheader("4. Target 변수 지정")

    st.markdown("질문 7: 분석할 Target 변수를 선정하셨나요?")
    st.checkbox("예, '추가 탐사 준비' 섹션에서 '관심 있는 열을 선택' 옵션을 사용하여 Target 변수를 선택했습니다.")


