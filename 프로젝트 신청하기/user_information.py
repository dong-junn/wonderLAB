import streamlit as st
import json
import os


def page():
    # 현재 파일의 디렉토리 경로를 구합니다.
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 동일한 디렉토리에 있는 JSON 파일의 경로를 구성합니다.
    json_file_path = os.path.join(current_dir, 'user_information.json')

    with open(json_file_path, 'r', encoding='utf-8') as file:
        user_info = json.load(file)

    # # 사용자 AI 수준 선택
    # ai_level_options = ('초심자', '데이터 보유자', '개발자')
    # if '1' not in st.session_state:
    #     st.session_state['1'] = ai_level_options[0]

    def update_ai_level_selection():
        # 선택된 AI 수준을 session_state에 저장
        # 여기서는 'selected_ai_level'이 selectbox에서 선택된 값을 저장하는 키라고 가정합니다.
        st.session_state['ai_level'] = st.session_state['selected_ai_level']

    # 사용자 AI 수준 선택을 위한 기본값 설정
    if 'ai_level' not in st.session_state:
        st.session_state['ai_level'] = next(iter(user_info['ai_level']['user']))

    # 사용자 옵션 목록을 사전의 키로부터 리스트로 변환
    options_list = list(user_info['ai_level']['user'].keys())

    # selectbox를 정의할 때, 'selected_ai_level'을 사용하여 선택된 값을 임시 저장
    st.selectbox(
        label=user_info['ai_level']['description'],
        options=options_list,
        index=options_list.index(st.session_state['ai_level']) if st.session_state['ai_level'] in options_list else 0,
        key='selected_ai_level',  # selectbox 선택값을 임시 저장할 키
        on_change=update_ai_level_selection
    )

    # 신분 선택
    if st.session_state['1'] in user_info['ai_level']['user']:
        status_options = list(user_info['ai_level']['user'][st.session_state['1']])

        if 'activity_field' not in st.session_state or st.session_state.activity_field not in status_options:
            st.session_state.activity_field = status_options[0]

        st.selectbox(
            '신분을 선택하세요',
            status_options,
            index=status_options.index(
                st.session_state.activity_field) if st.session_state.activity_field in status_options else 0,
            key='activity_field'
        )

    # 3. 경력 선택 (학생이 아닌 경우)
    if st.session_state.get('activity_field', '') != '학생':
        career_options = ('~5년', '5~10년', '10~20년')
        st.selectbox(
            '경력을 선택해주세요',
            career_options,
            index=career_options.index(
                st.session_state.career) if 'career' in st.session_state and st.session_state.career in career_options else 0,
            key='career'
        )

    # 4. 세부 신분 선택 (학생인 경우)
    if st.session_state.get('activity_field', '') == '학생':
        student_status_options = list(user_info['ai_level']['user'][st.session_state.ai_level]['학생'].keys())
        st.selectbox(
            "학생이시군요, 자세한 신분을 알려주세요",
            student_status_options,
            index=student_status_options.index(
                st.session_state.detailed_student_status) if 'detailed_student_status' in st.session_state and st.session_state.detailed_student_status in student_status_options else 0,
            key='detailed_student_status'
        )

    # 5. 목적 선택
    purpose_options = []
    if st.session_state.ai_level in user_info['ai_level']['user']:
        if st.session_state.get('activity_field', '') == '학생' and 'detailed_student_status' in st.session_state:
            purpose_options = user_info['ai_level']['user'][st.session_state.ai_level]['학생'][
                st.session_state.detailed_student_status]
        elif st.session_state.activity_field in user_info['ai_level']['user'][st.session_state.ai_level]:
            purpose_options = user_info['ai_level']['user'][st.session_state.ai_level][st.session_state.activity_field]

        st.multiselect(
            'AI를 적용하려는 목적을 선택하세요',
            purpose_options,
            default=[purpose for purpose in st.session_state.get('selected_purposes', []) if
                     purpose in purpose_options],
            key='selected_purposes'
        )

    # Displaying the selected purposes
    st.session_state.selected_purposes_str = ', '.join(st.session_state.get('selected_purposes', []))
    st.write("-----")
    st.subheader(f"1. AI습득 정도 선택 : {st.session_state.ai_level}")
    st.subheader(f"2. 신분 선택 : {st.session_state.get('activity_field', '정보 없음')}")
    st.subheader(f"3. 목적 선택 : {st.session_state.selected_purposes_str}")
