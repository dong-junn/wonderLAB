import streamlit as st
import json
import os


def page():
    if 'ai_level' not in st.session_state:
        st.session_state['ai_level'] = None
    if 'activity_field' not in st.session_state:
        st.session_state['activity_field'] = None
    if 'detailed_student_status' not in st.session_state:
        st.session_state['detailed_student_status'] = None
    if 'selected_purposes' not in st.session_state:
        st.session_state['selected_purposes'] = []
    # 현재 파일의 디렉토리 경로를 구합니다.
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 동일한 디렉토리에 있는 JSON 파일의 경로를 구성합니다.
    json_file_path = os.path.join(current_dir, 'user_information.json')

    with open(json_file_path, 'r', encoding='utf-8') as file:
        user_info = json.load(file)

    # 1. 사용자 AI 수준 선택
    ai_level_keys = list(user_info['ai_level']['user'].keys())
    ai_level_default_index = 0 if st.session_state['ai_level'] not in ai_level_keys else ai_level_keys.index(st.session_state['ai_level'])
    ai_level = st.selectbox(
        user_info['ai_level']['description'],
        ai_level_keys,
        index=ai_level_default_index
    )
    st.session_state['ai_level'] = ai_level

    # 2. 신분 선택
    status_options = list(user_info['ai_level']['user'][ai_level].keys()) if ai_level in user_info['ai_level']['user'] else []
    activity_field = st.selectbox(
        '신분을 선택하세요',
        status_options,
        index=status_options.index(st.session_state['activity_field']) if st.session_state['activity_field'] in status_options else 0
    )
    st.session_state['activity_field'] = activity_field

    detailed_student_status = None
    if activity_field == '학생':
        # 학생인 경우, 세부 신분 선택
        student_status_options = list(user_info['ai_level']['user'][ai_level]['학생'].keys())
        # session_state에 저장된 값이 현재 옵션 리스트에 있는지 확인합니다.
        if st.session_state['detailed_student_status'] not in student_status_options:
            st.session_state['detailed_student_status'] = student_status_options[0] if student_status_options else None
        detailed_student_status = st.selectbox(
            "학생이시군요, 자세한 신분을 알려주세요",
            student_status_options,
            index=student_status_options.index(
                st.session_state['detailed_student_status']) if student_status_options else 0
        )
        st.session_state['detailed_student_status'] = detailed_student_status

    # 3. 목적 선택
    purpose_options = []
    if activity_field == '학생' and detailed_student_status:
        # 학생의 세부 신분에 따른 목적 선택
        purpose_options = user_info['ai_level']['user'][ai_level]['학생'][detailed_student_status]
    elif activity_field in user_info['ai_level']['user'][ai_level]:
        # 일반 신분에 따른 목적 선택
        purpose_options = user_info['ai_level']['user'][ai_level][activity_field]

    selected_purposes = st.multiselect(
        'AI를 적용하려는 목적을 선택하세요',
        purpose_options,
        default=[purpose for purpose in st.session_state['selected_purposes'] if purpose in purpose_options]
    )
    st.session_state['selected_purposes'] = selected_purposes

    selected_purposes_str = ', '.join(selected_purposes)
    st.write("-----")
    st.subheader(f"**1. AI습득 정도 선택 : {ai_level}**")
    st.subheader(f"**2. 신분 선택 : {activity_field}**")
    st.subheader(f"**3. 목적 선택 : {selected_purposes_str}**")





