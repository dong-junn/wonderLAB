import streamlit as st 
import json


# JSON 파일 경로 설정
json_file_path = 'json/pages/user_group.json'

# JSON 파일 로드
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

def project_progress_user_group_selection():
    
    col1_data = data["col_1"]["expander_1"]
    col2_data = data["col_2"]["expander_2"]
    questions = col1_data["questions"]
    
    st.header(col1_data["header"])  
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander(col1_data["description"]):                                 
            selected_user_group = st.radio(
                col1_data["radioTitle"],
                col1_data["userGroupSelection"],
                label_visibility="hidden"
            )
        
            if st.button(col1_data["buttonText"], key='level'):
                st.write(col1_data["introMessage"])
                for question in questions[selected_user_group]:
                    message = st.chat_message("assistant")
                    message.write(question)
   
    with col2:
        with st.expander(col2_data["description"]):    
            selected_proj_field = st.radio(
                col2_data["radioTitle"],
                col2_data["userGroupSelection"],
                label_visibility="hidden"
            )
            
            if st.button(col2_data["buttonText"], key='purpose'):
                st.write(col2_data["introMessage"])
                for question in col2_data["questions"]:
                    message = st.chat_message("assistant")
                    message.write(question)
                

