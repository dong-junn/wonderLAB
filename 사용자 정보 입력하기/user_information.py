import streamlit as st 
import json
import os

# 현재 파일의 디렉토리 경로를 구합니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 동일한 디렉토리에 있는 JSON 파일의 경로를 구성합니다.
json_file_path = os.path.join(current_dir, 'user_information.json')

with open(json_file_path, 'r', encoding='utf-8') as file:
    user_info = json.load(file)

def page():
           
    # 1. 사용자 AI 수준 선택
    ai_level = st.selectbox(
        user_info['ai_level']['description'],
        user_info['ai_level']['user']
        )

    
    # 2. 신분 선택
    if ai_level in user_info['ai_level']['user']:
        status_options = list(user_info['ai_level']['user'][ai_level].keys())
        activity_field = st.selectbox(
            '신분을 선택하세요',
            status_options
        )

        detailed_student_status = None
        if activity_field == '학생':
            # 학생인 경우, 세부 신분 선택
            student_status_options = list(user_info['ai_level']['user'][ai_level]['학생'].keys())
            detailed_student_status = st.selectbox(
                "학생이시군요, 자세한 신분을 알려주세요",
                student_status_options
            )

    # 3. 목적 선택
    if ai_level in user_info['ai_level']['user']:
        purpose_options = []
        if activity_field == '학생' and detailed_student_status:
            # 학생의 세부 신분에 따른 목적 선택
            purpose_options = user_info['ai_level']['user'][ai_level]['학생'][detailed_student_status]
        elif activity_field in user_info['ai_level']['user'][ai_level]:
            # 일반 신분에 따른 목적 선택
            purpose_options = user_info['ai_level']['user'][ai_level][activity_field]
        
        selected_purposes = st.multiselect(
            'AI를 적용하려는 목적을 선택하세요',
            purpose_options
        )
        
    # 학생 선택 여부에 따라 슬라이더 설정 변경
    if activity_field == '학생':
        # 학생인 경우, 학년 선택 슬라이더
        slider_info = user_info['slider_student']['setting']
        slider = st.slider(
            user_info['slider_student']['description'],
            slider_info['min'], slider_info['max'], slider_info['step']
        )
    else:
        # 학생이 아닌 경우, 경력 선택 슬라이더
        slider_info = user_info['slider_worker']['setting']
        slider = st.slider(
            user_info['slider_worker']['description'],
            slider_info['min'], slider_info['max'], slider_info['step']
        )

    
    
    
    selected_purposes_str = ', '.join(selected_purposes)
    st.write("-----")
    st.write(f"**1. :green[AI습득 정도 선택] : :orange[{ai_level}]**")
    st.write(f"**2. :green[신분 선택] : :orange[{activity_field}]**")
    st.write(f"**3. :green[목적 선택] : :orange[{selected_purposes_str}]**")

    # '학생'을 선택한 경우 '학년'을, 그 외에는 '경력'을 표시
    if activity_field == '학생' and detailed_student_status:
        st.write(f"**4. :green[학년] : :orange[{slider}학년]**")
    else:
        st.write(f"**4. :green[경력] : :orange[{slider}년]**")

    


