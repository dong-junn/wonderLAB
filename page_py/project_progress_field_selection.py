import streamlit as st 
import json

# JSON 파일 경로 설정
json_file_path = 'json/pages/user_category.json'

# JSON 파일 로드
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

multi_select = data["multi_select"]

def project_progress_field_selection():
    st.header('제작하고 싶은 프로젝트 분야를 선택해주세요')
            

        
    multi_user_selection = st.multiselect(
        multi_select["description"],  
        multi_select["menu"]
    )
    
    if st.button('설정하기', key='level'):
        st.write('설정되었습니다')
    






