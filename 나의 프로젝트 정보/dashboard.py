import streamlit as st


def page():
    # session_state의 user_selections 초기화
    if 'user_selections' not in st.session_state:
        st.session_state['user_selections'] = {
            'ai_level': '',
            'career': '',
            'status': '',
            'detailed_status': '',
            'purposes': []
        }
    st.title("나의 프로젝트 정보")

    user_selections = st.session_state['user_selections']

    # 사용자의 선택된 AI 수준, 경력, 신분 등을 사용합니다.
    ai_level = user_selections['ai_level']
    career = user_selections['career']
    status = user_selections['status']
    detailed_status = user_selections.get('detailed_status')  # 'detailed_status' 키가 없을 수도 있으므로 get 메소드를 사용
    purposes = user_selections['purposes']

    # 여기서 사용자의 선택을 가지고 로직을 실행합니다.
    st.write(f"선택한 AI 수준: {ai_level}")
    st.write(f"선택한 경력: {career}")
    st.write(f"선택한 신분: {status}")
    if detailed_status:
        st.write(f"선택한 세부 신분: {detailed_status}")
    st.write(f"선택한 목적: {', '.join(purposes)}")





