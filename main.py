import streamlit as st
import json
import importlib
import sys
import os
from streamlit_option_menu import option_menu
import streamlit_antd_components as sac

# 현재 스크립트의 디렉토리 경로를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)  # 현재 디렉토리를 모듈 경로에 추가합니다.

# json 로드
with open('main.json', 'r', encoding='utf-8') as file:
    main_json = json.load(file)

# Sidebar 스타일 적용
st.markdown(main_json['sidebar']['style']['markdown'], unsafe_allow_html=True)
# st.sidebar.title("유통계산기 ver.1")
with st.sidebar.expander("Wonder_LAB", expanded=True):
    st.session_state.page = sac.menu([
        sac.MenuItem('협회소개', icon='house-fill'),
        sac.MenuItem('AI 프로젝트 안내', icon='box-fill', children=[
            sac.MenuItem('프로젝트 둘러보기', icon='apple'),
            sac.MenuItem('프로젝트 신청하기', icon='apple'),
            sac.MenuItem('3분 테스트 도전', icon='apple'),
        ]),
        sac.MenuItem('AI 프로젝트 실전', icon='box-fill', children=[
            sac.MenuItem('프로젝트 주제선택', icon='apple'),
            sac.MenuItem('나만의 AI 설계', icon='apple'),
            sac.MenuItem('효율성 판단지표 생성', icon='apple'),
            sac.MenuItem('데이터 셋 연습', icon='apple'),
            sac.MenuItem('AI 모델 생성', icon='apple'),
            sac.MenuItem('AI 적용 시뮬레이션', icon='apple'),
        ]),
        sac.MenuItem('MY 정보', icon='box-fill', children=[
            sac.MenuItem('내 프로젝트 현황(정보/등록)', icon='apple'),
            sac.MenuItem('인증서 발급', icon='apple'),
            sac.MenuItem('평가서 제출', icon='apple'),
        ]),
    ], color='yellow', format_func='title', open_all=False, return_index=True)

# 현재 페이지번호 확인하는용도
st.write(f"{st.session_state.page}")
# 페이지번호를 통하여 각 페이지를 연결시키는 방식
if st.session_state.page == 1:
    ""

# Sidebar 구성
with st.sidebar:
    with st.expander("HOME", expanded=True):
        selected_option = option_menu(
            main_json['sidebar']['name'],
            options=list(main_json['pages'].keys()),
            icons=main_json['sidebar']['icons'],
            menu_icon=main_json['sidebar']['menu_icon'],
            default_index=0,
            styles={**main_json['sidebar']['style']['css']}
        )
        st.write(st.session_state)

if selected_option is not None:
    # 선택된 페이지의 소스 파일명을 가져옵니다.
    file_name = main_json['pages'].get(selected_option)
    if file_name:
        # 모듈 경로를 폴더명과 소스 파일명으로부터 구성합니다.
        module_path = f"{selected_option}.{file_name}"
        try:
            # 모듈을 가져옵니다.
            module = importlib.import_module(module_path)
            # 모듈 내의 main 함수를 호출합니다.
            if hasattr(module, 'page'):
                module.page()

            else:
                st.error(f"Error: 'main' function not found in the module '{module_path}'.")
        except ModuleNotFoundError as e:
            st.error(f"Module not found: {e}")
            # 적절한 오류 메시지 또는 로그를 남기는 코드를 추가할 수 있습니다.
    else:
        st.error(f"No module information found for selected option: {selected_option}")
        # 선택된 옵션에 대한 모듈 정보가 없을 때의 처리를 추가합니다.
