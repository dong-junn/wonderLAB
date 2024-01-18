import streamlit as st

st.title("AI 적용 가이드")
st.write("AI를 여러분의 분야에 적용하기 위한 정보를 입력해 주세요.")

# 1. 사용자 AI 수준 선택
ai_level = st.selectbox('당신의 AI에 대한 수준은?', ['초심자', '데이터 보유자', '개발자'])

# 2. 신분 선택
status = st.selectbox('신분을 선택하세요', ['직장인', '대학생', '고등학생', '연구자', '농민', 'CEO', '기타'])

# 3. 경력 또는 관련 경험 선택
if status == '직장인':
    experience = st.selectbox('경력년도를 선택하세요', ['1년 미만', '1-3년', '3-5년', '5년 이상'])
else:
    experience = st.slider('관련 경험 또는 학습 수준', 0, 10, 1)

# 4. 목적 선택
purpose = st.multiselect('AI를 적용하려는 목적을 선택하세요', ['노동력 감소', '생산력 향상', '데이터 분석', '새로운 기술 습득', '기타'])

# 입력 결과 요약
st.write("-----")
st.write("입력 요약:")
st.write(f"AI 수준: {ai_level}")
st.write(f"신분: {status}")
st.write(f"경력 또는 경험: {experience}")
st.write(f"목적: {', '.join(purpose)}")
