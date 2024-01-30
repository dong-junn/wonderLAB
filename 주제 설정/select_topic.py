import streamlit as st 
import json
import os
from PIL import Image


# Streamlit UI 구성
def page():
    st.subheader("AI를 활용하여 사업체의 제품이나 업무 방식을 강화하는 몇 가지 실제 예시를 고려해 볼 수 있습니다.")
    st.subheader("ㆍNetflix의 개인화된 추천 시스템")
    st.subheader("    Netflix는 머신러닝과 데이터 분석을 활용하여 사용자의 시청 기록, 검색 기록 및 평가 등 다양한 데이터 포인트를 분석합니다. 이를 통해 사용자에게 맞춤형 추천을 제공하며, 이는 고객 유지와 신규 가입자 유치에 크게 기여하고 있습니다. Netflix는 이 시스템이 플랫폼에서 시청되는 콘텐츠의 80%를 차지한다고 밝히며, 고객 유지 비용을 10억 달러 이상 절약했다고 추정합니다.")

    st.subheader("ㆍSephora의 AI 활용 뷰티 산업 혁신")
    st.subheader(" Sephora는 웹사이트와 모바일 앱에 챗봇을 도입하여, 머신러닝 알고리즘을 사용해 고객 경험을 개인화하고 지원 및 추천을 제공합니다. 'Sephora Virtual Artist'는 얼굴 인식 기술을 사용하여 고객이 다양한 화장품을 시험해 볼 수 있도록 도와줍니다. 이러한 AI 도구는 고객 만족도와 매출을 개선하는 데 기여하고 있습니다.")

    st.subheader("ㆍCoca-Cola의 맞춤형 마케팅 캠페인")
    st.subheader(" Coca-Cola는 제품 포장과 유통을 최적화하기 위해 머신러닝을 사용합니다. 회사는 데이터 분석을 통해 고객 선호도의 패턴을 식별하고, 다양한 시장과 인구 통계에 맞는 특정 제품 포장 및 유통 전략을 추천합니다. 이 접근 방식은 판매 및 유통 효율성을 최대 30% 향상시켰으며, 더 타겟된 캠페인과 메시징을 개발하는 데 도움이 되었습니다.")

    st.subheader("ㆍUnilever의 소셜 미디어 광고 최적화")
    st.subheader("Unilever는 소셜 미디어 플랫폼에서의 데이터를 분석하여 다양한 인구 통계 및 시장에 대한 가장 효과적인 광고 전략을 식별하는 AI 시스템을 개발했습니다. 이러한 접근 방식으로 Unilever는 광고 성능을 크게 향상시켰으며, 일부 캠페인은 참여도와 클릭률에서 최대 50%의 증가를 보였습니다.")

    st.subheader("이러한 예시들은 AI가 마케팅 전략을 최적화하고, 비즈니스 결과를 크게 개선하는 데 어떻게 기여할 수 있는지 보여줍니다. AI는 더 개인화되고 타겟화된 경험을 제공함으로써 고객 만족도를 개선하고, 광고 및 유통 전략을 최적화하여 ROI를 향상시킬 수 있습니다.")

    st.subheader("1. 질문: 인공지능을 활용하려는 주된 목적은 무엇인가요?")
    st.subheader("선택지:")
    st.subheader("강점 강화: 회사의 제품이나 서비스의 질 향상, 시장에서의 경쟁 위치 강화, 업무 시스템의 효율성 및 효과성 증진, 개인 또는 팀의 업무 능력 및 성과 향상")
    st.subheader("문제 해결: 업무상의 병목 현상, 비효율성, 또는 기타 문제 해결, 고객 대응 및 서비스 품질 개선, 제품 또는 서비스의 품질 관리 및 개선")

    st.subheader("2. 질문: 인공지능을 통해 어떤 종류의 효율성을 기대하시나요?")
    st.subheader("선택지:")
    st.subheader("오류 개선: 오류율 감소, 정확도 향상")
    st.subheader("시간 절감: 작업 처리 시간 단축, 대기 시간 최소화")
    st.subheader("비용 절감: 운영 비용 감소, 자원 최적화")
    st.subheader("비용 절감: 운영 비용 감소, 자원 최적화")

    st.subheader("3. 질문: 당신의 업무 방식과 순서는 어떻게 되나요?")
    st.subheader("선택지:")
    st.subheader("데이터로 정보를 받고 대응하는 업무: 정보 수집, 응답 및 대응")
    st.subheader("데이터 분석을 기반으로 결정하는 업무: 분석, 예측, 전략 결정")
    st.subheader("데이터를 만들어 제공하는 업무: 콘텐츠 생성, 보고서 작성, 정보")


    """
    tem1 = Image.open("images/주제선정2.png")
    st.image(tem1)

    tem2 = Image.open("images/주제선정1.jpg")
    st.image(tem2)

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