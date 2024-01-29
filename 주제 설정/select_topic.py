import streamlit as st 
import json
import os
from PIL import Image


# Streamlit UI 구성
def page():
    tem1 = Image.open("images/주제선정2.png")
    st.image(tem1)

    tem2 = Image.open("images/주제선정1.jpg")
    st.image(tem2)





    """
        # 현재 파일의 디렉토리 경로를 구합니다.
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 동일한 디렉토리에 있는 JSON 파일의 경로를 구성합니다.
    json_file_path = os.path.join(current_dir, 'select_topic.json')

    # JSON 파일을 불러옵니다.
    with open(json_file_path, 'r', encoding='utf-8') as file:
        topics = json.load(file)

    st.subheader("인공지능 모델의 기능과 업무 개선 질문")
    option_1 = st.selectbox(
        "제한된 인공지능 모델의 어떤 기능이 현재의 업무 프로레스를 개선하는데 도움이 될 것 같나요?",
        ('데이터 분석 자동화', '고객 응대 최적화', '재고 예측 정확도 향상', '문서 처리 자동화',)

    )
    st.subheader("모델 도입에 따른 효율성 기대 질문")
    option_2 = st.selectbox(
        "해당 모델을 도입함으로써 당신의 사업체에서 어떤 효율성을 기대할 수 있나요?",
        ('작업 시간 절약', '오류율 감소', '고객 만족도 향상', '비용 절감')
    )

    option_3 = st.selectbox(
        "이 인공지능 모델이 구체적으로 어떤 업무 문제를 해결허거나 개선할 수 있을지 설명해주세요",
        ('고객 서비스 효율화', '제품 결함 식별', '판매 예측 정확성 개선', '업무 프로세스 자동화')
    )

    st.subheader("솔루션 사용 목표 설정 질문")
    option_4 = st.selectbox(
        "이 솔루션을 사용하여 달성하고자 하는 주요 목표는 무엇인가요?",
        ('생산성 향상', '고객 경험 개선', '업무 오류 최소화', '비즈니스 인사이트 확보')
    )

    option_5 = st.selectbox(
        "업무 개선의 목적은 무엇인가요?",
        ('시간 절약', '노동력 및 비용 절감', '자동화', '업무 품질 향상')
    )


    st.title("주제 선택하기")

    def json_to_html(topics):
        # 모든 프로젝트의 title 목록을 추출
        project_titles = [project['title'] for project in topics]

        # Selectbox를 통해 사용자가 프로젝트를 선택할 수 있도록 함
        selected_title = st.selectbox('프로젝트를 선택하세요', project_titles)

        # 선택된 프로젝트 정보 찾기
        selected_project = next(project for project in topics if project['title'] == selected_title)

        # 선택된 프로젝트의 정보를 HTML로 변환
        html_content = "<div style='margin: 10px;'>"
        html_content += f"<div style='margin-bottom: 20px;'><h3>{selected_project['title']}</h3><ul>"
        for key, value in selected_project.items():
            if key != 'title':
                html_content += f"<li><b>{key}:</b> {value}</li>"
        html_content += "</ul></div>"
        html_content += "</div>"

        return html_content

    html_data = json_to_html(topics)
    st.markdown(html_data, unsafe_allow_html=True)

"""