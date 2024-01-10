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


                '''if selected_user_group == "연구자/회사 재직자":                   
                    # 문제정의
                    message.write("어떠한 업무 관련 문제를 가지고 계신가요?")
                    message.write("이 문제는 어떻게 업무 효율성이나 성과에 영향을 미치나요?")
                    # 문제의 지속성
                    message.write("이 문제는 지속적으로 발생하는 것인가요?")
                    message.write("문제가 지속된다면, 그 주된 원인이 무엇이라고 생각하시나요?")
                    # 데이터 분석의 어려움
                    message.write("이 문제를 해결하는 데 데이터 분석이 필요하다고 생각하시나요?")
                    message.write("데이터 분석에 대한 어려움이나 필요한 선진 분석 기술이 무엇인지 말씀해 주세요.")
                    # 데이터 접근성
                    message.write("해당 문제와 관련된 데이터를 보유하고 계신가요?")
                    message.write("필요한 데이터를 수집하거나 접근하는 데 어떤 도전이 있나요?")
                                            
                if selected_user_group == "AI 기반 웹사이트/웹앱 개발자":
                    # 문제정의
                    message.write("어떠한 개발 관련 문제를 직면하고 계신가요?")
                    message.write("이 문제는 개발 프로젝트의 어떤 측면에 영향을 미치나요?")
                    # AI 모델링의 어려움
                    message.write("AI 모델을 직접 코딩하는 데 있어 어떤 기술적 어려움이 있나요?")
                    message.write("이러한 어려움을 극복하기 위해 필요한 기술 또는 지식은 무엇인가요?")
                    # 데이터 접근성 및 활용
                    message.write("해당 문제에 관련된 데이터를 가지고 계신가요, 또는 쉽게 구할 수 있나요?")
                    message.write("이 데이터를 활용하여 AI 모델을 개발하거나 향상시키기 위한 구체적인 계획이 있으신가요?")'''

    
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
                

