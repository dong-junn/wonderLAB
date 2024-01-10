import streamlit as st
import importlib
import json
from streamlit_option_menu import option_menu

# json 로드
with open('json/call_menu-section.json', 'r', encoding='utf-8') as file:
    main_UI = json.load(file)


with open('json/menu-section_styles.json', 'r', encoding='utf-8') as file:
    UI_style = json.load(file)




st.set_page_config(layout="wide", initial_sidebar_state="auto")

st.markdown(UI_style['styles']['markdown'], unsafe_allow_html=True)

# 메뉴 이름들을 추출하여 options 리스트에 저장
options = list(main_UI.keys())

with st.sidebar:
    with st.expander("HOME",expanded=True):   
        selected_option = option_menu(
            'Wonder Lab ',           
            options = options,   
            icons=['house-fill',], 
            menu_icon='chat-text-fill',
            default_index=0,
            styles={**UI_style['styles']['sidebar']}
            
            )
    with st.expander("JSON"):
        json = option_menu(
            '예시',
            options=['다운로드']
            )

if selected_option is not None:
    module_info = main_UI.get(selected_option)  # .get() 메서드로 안전하게 딕셔너리 값을 추출
    if module_info:
        module_name = module_info["module"]
        module = importlib.import_module(f'page_py.{module_name}')
        page_function_name = f'{module_name}'
        page_function = getattr(module, page_function_name)
        page_function()  # 해당 페이지 함수 호출







