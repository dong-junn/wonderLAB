import streamlit as st 
import json
import os

# 현재 파일의 디렉토리 경로를 구합니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 동일한 디렉토리에 있는 JSON 파일의 경로를 구성합니다.
json_file_path = os.path.join(current_dir, 'select_topic.json')

with open(json_file_path, 'r', encoding='utf-8') as file:
    json_navi = json.load(file)

multi_select = json_navi["multi_select"]

def page():
    # 0. 업무 분야
    business_field = st.selectbox('업무 분야는 뭔가요?', ['IT', '마케팅', '교육', '연구', '기타'])

    # 1. 업무 상세
    business_detail = st.text_input('당신의 업무는 무엇인가요?')

    # 2. 업무 과정
    business_process = st.text_input('업무의 과정은 어떻게 구성되어 있나요?')

    # 3. 필요 능력 및 비숙련 분야
    required_skills = st.text_input('업무에 필요한 능력은 무엇인가요?')
    unskilled_areas = st.text_input('비숙련되는 분야와 능력은 무엇인가요?')









