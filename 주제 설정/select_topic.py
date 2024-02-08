import streamlit as st 


# Streamlit UI 구성
def page():
    st.subheader("AI를 활용하여 사업체의 제품이나 업무 방식을 강화하는 몇 가지 실제 예시를 고려해 볼 수 있습니다.")
    st.subheader("ㆍNetflix의 개인화된 추천 시스템")
    st.write("    Netflix는 머신러닝과 데이터 분석을 활용하여 사용자의 시청 기록, 검색 기록 및 평가 등 다양한 데이터 포인트를 분석합니다. 이를 통해 사용자에게 맞춤형 추천을 제공하며, 이는 고객 유지와 신규 가입자 유치에 크게 기여하고 있습니다. Netflix는 이 시스템이 플랫폼에서 시청되는 콘텐츠의 80%를 차지한다고 밝히며, 고객 유지 비용을 10억 달러 이상 절약했다고 추정합니다.")

    st.subheader("ㆍSephora의 AI 활용 뷰티 산업 혁신")
    st.write(" Sephora는 웹사이트와 모바일 앱에 챗봇을 도입하여, 머신러닝 알고리즘을 사용해 고객 경험을 개인화하고 지원 및 추천을 제공합니다. 'Sephora Virtual Artist'는 얼굴 인식 기술을 사용하여 고객이 다양한 화장품을 시험해 볼 수 있도록 도와줍니다. 이러한 AI 도구는 고객 만족도와 매출을 개선하는 데 기여하고 있습니다.")

    st.subheader("ㆍCoca-Cola의 맞춤형 마케팅 캠페인")
    st.write(" Coca-Cola는 제품 포장과 유통을 최적화하기 위해 머신러닝을 사용합니다. 회사는 데이터 분석을 통해 고객 선호도의 패턴을 식별하고, 다양한 시장과 인구 통계에 맞는 특정 제품 포장 및 유통 전략을 추천합니다. 이 접근 방식은 판매 및 유통 효율성을 최대 30% 향상시켰으며, 더 타겟된 캠페인과 메시징을 개발하는 데 도움이 되었습니다.")

    st.subheader("ㆍUnilever의 소셜 미디어 광고 최적화")
    st.write("Unilever는 소셜 미디어 플랫폼에서의 데이터를 분석하여 다양한 인구 통계 및 시장에 대한 가장 효과적인 광고 전략을 식별하는 AI 시스템을 개발했습니다. 이러한 접근 방식으로 Unilever는 광고 성능을 크게 향상시켰으며, 일부 캠페인은 참여도와 클릭률에서 최대 50%의 증가를 보였습니다.")

    st.write("이러한 예시들은 AI가 마케팅 전략을 최적화하고, 비즈니스 결과를 크게 개선하는 데 어떻게 기여할 수 있는지 보여줍니다. AI는 더 개인화되고 타겟화된 경험을 제공함으로써 고객 만족도를 개선하고, 광고 및 유통 전략을 최적화하여 ROI를 향상시킬 수 있습니다.")
    st.title("")

    if 'purpose1' not in st.session_state:
        st.session_state['purpose1'] = '강점강화'
    def update_purpose1_selection(new_value):
        st.session_state['purpose1'] = new_value

    # selectbox 위젯
    st.session_state['purpose1'] = st.selectbox(
        "선택해주세요",
        ('강점강화', '문제해결'),
        index=('강점강화', '문제해결').index(st.session_state['purpose1']),  # session_state의 값을 기본값으로 사용
        on_change=update_purpose1_selection,  # 선택이 바뀌면 호출될 콜백 함수 지정
        args=(st.session_state['purpose1'],)  # 콜백 함수에 전달될 인자
    )

    if st.session_state['purpose1'] == '강점강화':
        st.write("회사의 제품이나 서비스의 질 향상, 시장에서의 경쟁 위치 강화, 업무 시스템의 효율성 및 효과성 증진, 개인 또는 팀의 업무 능력 및 성과 향상")
    elif st.session_state['purpose1'] == '문제해결':
        st.write("업무상의 병목 현상, 비효율성, 또는 기타 문제 해결, 고객 대응 및 서비스 품질 개선, 제품 또는 서비스의 품질 관리 및 개선")





    st.subheader("2. 인공지능을 통해 어떤 종류의 효율성을 기대하시나요?")
    # purpose2 초기화 및 selectbox 설정
    if 'purpose2' not in st.session_state:
        st.session_state['purpose2'] = '오류 개선'
    #def update_purpose2_selection(new_value):
        #st.session_state['purpose2'] = new_value


    st.session_state['purpose2'] = st.selectbox(
        "선택해주세요",
        ('오류 개선', '시간 절감', '비용 절감', '인력 절감'),
        index=('오류 개선', '시간 절감', '비용 절감', '인력 절감').index(st.session_state['purpose2']),

        args=(st.session_state['purpose2'],)
    )

    # 선택에 따른 메시지 출력
    if st.session_state['purpose2'] == '오류 개선':
        st.write("오류율 감소, 정확도 향상")

    elif st.session_state['purpose2'] == '시간 절감':
        st.write("작업 처리 시간 단축, 대기 시간 최소화")

    elif st.session_state['purpose2'] == '비용 절감':
        st.write("운영 비용 감소, 자원 최적화")

    elif st.session_state['purpose2'] == '인력 절감':
        st.write("자동화를 통한 인력 필요량 감소")


    # work_type 초기화 및 selectbox 설정
    if 'work_type' not in st.session_state:
        st.session_state['work_type'] = '데이터로 정보를 받고 대응하는 업무'
    st.selectbox(
        "선택해주세요",
        ('데이터로 정보를 받고 대응하는 업무', '데이터 분석을 기반으로 결정하는 업무', '데이터를 만들어 제공하는 업무'),
        key='work_type'
    )

    # work_order 초기화 및 selectbox 설정
    if 'work_order' not in st.session_state:
        st.session_state['work_order'] = '업무를 모두 직접 진행'
    st.selectbox(
        "선택해주세요",
        ('업무를 모두 직접 진행', '업무를 팀원들에게 지시', '업무를 진행할 수 있도록 준비 및 자료 제공', '제공된 업무 관련 분석 자료 기반으로 최종 의사결정'),
        key='work_order'
    )

    # main_function 초기화 및 selectbox 설정
    if 'main_function' not in st.session_state:
        st.session_state['main_function'] = '예측이 필요하거나 가능한 업무'
    st.selectbox(
        "선택해주세요",
        ('예측이 필요하거나 가능한 업무', '분류가 필요하거나 가능한 업무', '시각적인 요약이 필요한 업무', '창의력을 기반으로 생성 업무'),
        key='main_function'
    )

    # ai_benefits 초기화 및 selectbox 설정
    if 'ai_benefits' not in st.session_state:
        st.session_state['ai_benefits'] = '시간 대비 생산성 향상'
    st.selectbox(
        "선택해주세요",
        ('시간 대비 생산성 향상', '최종 결정을 위한 합리적 판단 근거 제공', '업무의 단순화', '자신의 현재 업무 대체가 아닌 본인 업무 능력 향상'),
        key='ai_benefits'
    )

    # Display the summary of selections
    st.divider()
    st.subheader(f"1: {st.session_state.purpose1}")
    st.subheader(f"2: {st.session_state.purpose2}")
    st.subheader(f"3: {st.session_state.work_type}")
    st.subheader(f"4: {st.session_state.work_order}")
    st.subheader(f"5: {st.session_state.main_function}")
    st.subheader(f"6: {st.session_state.ai_benefits}")

