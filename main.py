import streamlit as st
import json
import importlib
import sys
import os
from streamlit_option_menu import option_menu

# 현재 스크립트의 디렉토리 경로를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)  # 현재 디렉토리를 모듈 경로에 추가합니다.

# json 로드
with open('main.json', 'r', encoding='utf-8') as file:
    main_json = json.load(file)

#json navigation management via variable
name= main_json['sidebar']['name']
options = list(main_json['pages'].keys())
icons = main_json['sidebar']['icons']
menu_icon = main_json['sidebar']['menu_icon']
styles = {**main_json['sidebar']['style']['css']}

sidebar_style= main_json['sidebar']['style']['markdown']

# Sidebar 스타일 적용
st.markdown(sidebar_style, unsafe_allow_html=True)

# Sidebar 구성
with st.sidebar:
    with st.expander("HOME", expanded=True):   
        selected_option = option_menu(
            name,           
            options= options,   
            icons= icons, 
            menu_icon= menu_icon,
            default_index=0,
            styles= styles
        )


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



