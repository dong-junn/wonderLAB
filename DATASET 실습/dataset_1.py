import streamlit as st
from streamlit_chat import message


def page():
    st.title("데이터 수집 실습 과정")
    st.subheader("단계 1: 주제와 관련된 데이터 유형 결정")
    st.markdown("질문 1: 선택한 주제와 가장 밀접하게 관련된 데이터 유형을 결정하셨나요?")

    # 텍스트 데이터 체크박스
    text_data = st.checkbox("텍스트 데이터: 리뷰, 기사 등 텍스트 형식의 데이터를 선택했습니다.", key="text_data")
    # 수치 데이터 체크박스
    numeric_data = st.checkbox("수치 데이터: 통계, 측정값 등 수치로 표현되는 데이터를 선택했습니다.", key="numeric_data")

    # 이미지 또는 비디오 데이터 체크박스
    image_video_data = st.checkbox("이미지 또는 비디오 데이터: 시각적 정보를 포함하는 이미지나 비디오 데이터를 선택했습니다.", key="image_video_data")
    difficulty_1 = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_1")

    if difficulty_1:
        message("어려움을 설명해주세요.", key="message_1")
        message("사용자 입력", is_user=True, key="user_input_1")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_1")

    # 단계 2: 데이터 수집의 범위 설정
    st.subheader("단계 2: 데이터 수집의 범위 설정")
    st.markdown("질문 2: 데이터를 수집할 범위를 어떻게 설정하셨나요?")
    st.checkbox("넓은 범위: 모든 고객 리뷰와 같이 광범위한 데이터를 수집하기로 결정했습니다.", key="wide_range")
    st.checkbox("중간 범위: 특정 지역의 고객 리뷰와 같이 좀 더 구체적인 범위의 데이터를 선택했습니다.", key="medium_range")
    st.checkbox("매우 한정된 범위: 특정 시기의 고객 리뷰와 같이 매우 제한된 범위의 데이터를 선택했습니다.", key="narrow_range")

    difficulty_narrow = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_narrow")
    if difficulty_narrow:
        message("매우 한정된 범위 데이터 수집과 관련된 어려움을 설명해주세요.", key="message_narrow")
        message("사용자 입력", is_user=True, key="user_input_narrow")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_narrow")

    #3단계
    st.subheader("단계 3: 데이터 수집의 시간적 범위 결정")
    st.markdown("질문 3: 수집할 데이터의 시간적 범위를 어떻게 설정하셨나요?")
    # 장기간 데이터 체크박스
    long_term_data = st.checkbox("장기간 데이터: 지난 몇 년간의 데이터를 수집하기로 했습니다.", key="long_term_data")
    # 중기간 데이터 체크박스
    mid_term_data = st.checkbox("중기간 데이터: 최근 몇 달간의 데이터를 수집하기로 했습니다.", key="mid_term_data")
    # 단기간 데이터 체크박스
    short_term_data = st.checkbox("단기간 데이터: 최근 몇 주간의 데이터를 수집하기로 했습니다.", key="short_term_data")
    difficulty_short_term = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_short_term")
    if difficulty_short_term:
        message("단기간 데이터 수집과 관련된 어려움을 설명해주세요.", key="message_short_term")
        message("사용자 입력", is_user=True, key="user_input_short_term")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_short_term")

    #4단계
    st.subheader("단계 4: 데이터 수집 방법 선택")
    st.markdown("질문 4: 데이터를 수집할 방법을 어떻게 결정하셨나요?")
    # 온라인 데이터 수집 체크박스
    online_collection = st.checkbox("온라인 수집: 웹 크롤링, 온라인 설문 등을 통해 데이터를 수집하기로 했습니다.", key="online_collection")
    # 오프라인 데이터 수집 체크박스
    offline_collection = st.checkbox("오프라인 수집: 인터뷰, 서면 설문 등을 통해 데이터를 수집하기로 했습니다.", key="offline_collection")
    # 혼합 방식 데이터 수집 체크박스
    mixed_collection = st.checkbox("혼합 방식: 온라인 및 오프라인 데이터를 조합하여 수집하기로 했습니다.", key="mixed_collection")
    difficulty_mixed = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_mixed")
    if difficulty_mixed:
        message("혼합 방식 데이터 수집과 관련된 어려움을 설명해주세요.", key="message_mixed")
        message("사용자 입력", is_user=True, key="user_input_mixed")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_mixed")

    # 단계 5: 데이터 수집 후 처리 방법 결정
    st.subheader("단계 5: 데이터 수집 후 처리 방법 결정")
    st.markdown("질문 5: 데이터 수집 후 어떤 처리 과정을 계획하고 계신가요?")
    # 기본 처리 체크박스
    basic_processing = st.checkbox("기본 처리: 데이터를 정리하고 분류하는 기본적인 처리를 진행하기로 했습니다.", key="basic_processing")
    # 상세한 분석 체크박스
    detailed_analysis = st.checkbox("상세한 분석: 패턴 분석, 통계적 분석 등 상세한 데이터 분석을 수행하기로 했습니다.", key="detailed_analysis")
    # 고급 처리 체크박스
    advanced_processing = st.checkbox("고급 처리: 머신 러닝, 데이터 마이닝과 같은 고급 데이터 처리 기법을 적용하기로 했습니다.", key="advanced_processing")
    difficulty_advanced = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_advanced")
    if difficulty_advanced:
        message("고급 데이터 처리와 관련된 어려움을 설명해주세요.", key="message_advanced")
        message("사용자 입력", is_user=True, key="user_input_advanced")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_advanced")

    '''
    st.title(":orange[DATA 수집 실습]")

    st.title("")  # blank

    st.header(":green[목적 설정]")
    st.selectbox(
        ":violet[데이터셋의 사용 목적이 무엇인가요?]",
        ('식당 리뷰 분석', '날씨 패턴 예측',)
    )

    st.title("")

    st.header(":green[데이터 유형 결정]")
    st.selectbox(
        ":violet[수지할 데이터의 유형을 결정해주세요]",
        ('텍스트', '이미지', '수치')
    )

    st.title("")

    st.header(":green[데이터 수집 방법 결정]")
    st.selectbox(
        ":violet[데이터 수집 방법을 결정해주세요]",
        ('직접 수집', '온라인 수집')
    )

    st.title("")

    st.header(":green[데이터 입력]")
    st.file_uploader(
        ":violet[파일을 입력해주세요]",
        type=["xlsx"]
    )

    st.title("")

    message("gpt연결 예정")
    message("~~", is_user=True)
    with st.container():
        st.text_input("사용자 입력:")

    st.title("")

    st.link_button(":rainbow[AI Wonder 접속하기]", "http://magiccanaiv2-1212047460.ap-northeast-2.elb.amazonaws.com")
    '''

    st.title("최종 데이터셋 만들기 실습 과정 ")

    # 실습 단계 1: Target 변수 결정
    st.subheader("실습 단계 1: Target 변수 결정")
    st.markdown("질문 1: 데이터셋에서 분석하고자 하는 주요 목표인 Target 변수를 정하셨나요?")

    st.checkbox("매출액 또는 수익을 Target 변수로 정했습니다.", key="target_revenue")
    st.checkbox("고객 만족도 또는 사용자 참여도를 Target 변수로 선정했습니다.", key="target_customer_satisfaction")
    st.checkbox("제품의 품질 또는 서비스의 효율성을 중심으로 설정했습니다.", key="target_product_quality")
    difficulty_target_product_quality = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_target_product_quality")
    if difficulty_target_product_quality:
        message("제품의 품질 또는 서비스의 효율성에 대한 어려움을 설명해주세요.", key="message_target_product_quality")
        message("사용자 입력", is_user=True, key="user_input_target_product_quality")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_target_product_quality")

    # 실습 단계 2: 주요 변수 식별
    st.subheader("실습 단계 2: 주요 변수 식별")
    st.markdown("질문 2: Target 변수에 영향을 미칠 주요 변수들을 식별하고 엑셀에 기록하셨나요?")

    st.checkbox("가격, 프로모션, 할인율과 같은 마케팅 변수를 포함했습니다.", key="marketing_variables")
    st.checkbox("제품 특성, 고객 서비스의 질, 리뷰 등을 주요 변수로 기록했습니다.", key="product_features")
    st.checkbox("시장 동향, 경쟁사 활동, 경제 상황을 변수로 고려했습니다.", key="market_trends")
    difficulty_market_trends = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_market_trends")
    if difficulty_market_trends:
        message("시장 동향 및 경쟁사 활동 관련 변수 식별에 대한 어려움을 설명해주세요.", key="message_market_trends")
        message("사용자 입력", is_user=True, key="user_input_market_trends")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_market_trends")

    # 실습 단계 3: Target 및 주요 변수값 엑셀에 입력
    st.subheader("실습 단계 3: Target 및 주요 변수값 엑셀에 입력")
    st.markdown("질문 3: 선택한 변수들에 대해 총 30개의 값을 엑셀에 가로로 입력하셨나요?")
    st.checkbox("각 변수에 대해 30개의 값을 직접 가로로 입력했습니다.", key="input_30_values")
    st.checkbox("실제 데이터나 가상 데이터를 모든 변수에 대해 입력했습니다.", key="input_actual_or_simulated_data")
    st.checkbox("chatGPT에 변수명만 들어간 파일을 올리고, 가상의 값을 생성하도록 요청하여 변수값을 채웠습니다.", key="input_values_via_chatGPT")

    difficulty_input_values_via_chatGPT = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_input_values_via_chatGPT")
    if difficulty_input_values_via_chatGPT:
        message("chatGPT를 통한 변수값 입력에 대한 어려움을 설명해주세요.", key="message_input_values_via_chatGPT")
        message("사용자 입력", is_user=True, key="user_input_input_values_via_chatGPT")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_input_values_via_chatGPT")

    # 실습 단계 4: 데이터셋의 구조 확인 및 전처리
    st.subheader("실습 단계 4: 데이터셋의 구조 확인 및 전처리")
    st.markdown("질문 4: 엑셀에서 데이터셋의 구조를 검토하고 필요한 전처리를 수행하셨나요?")
    st.checkbox("모든 열과 행이 적절하게 배열되어 있는지 확인했습니다.", key="check_columns_rows")


    st.checkbox("데이터 형식과 단위가 일관되게 설정되었는지 검토했습니다.", key="check_data_format")


    st.checkbox("누락된 값이 없도록 데이터를 정제했습니다.", key="clean_missing_values")
    difficulty_clean_missing_values = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_clean_missing_values")
    if difficulty_clean_missing_values:
        message("데이터 정제에 대한 어려움을 설명해주세요.", key="message_clean_missing_values")
        message("사용자 입력", is_user=True, key="user_input_clean_missing_values")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_clean_missing_values")

    # 실습 단계 5: 데이터셋 저장 및 증폭 준비
    st.subheader("실습 단계 5: 데이터셋 저장 및 증폭 준비")
    st.markdown("질문 5: 완성된 데이터셋을 .csv 파일로 저장하고 증폭을 위해 준비하셨나요?")
    st.checkbox("데이터셋을 .csv 형식으로 저장했습니다. 파일 이름은 영어로 작성했습니다 (예: myfile.csv).", key="save_csv_format")
    st.checkbox("저장된 파일을 'AI wonder' 플랫폼에 업로드하기 위해 준비했습니다.", key="prepare_upload_ai_wonder")
    st.link_button("AI wonder로 이동하기", "http://magiccanaiv2-1212047460.ap-northeast-2.elb.amazonaws.com/")
    st.checkbox("증폭 기능을 사용하기 전에 파일 포맷과 데이터를 최종 확인했습니다.", key="check_format_before_amplification")

    difficulty_check_format_before_amplification = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_check_format_before_amplification")

    if difficulty_check_format_before_amplification:
        message("파일 포맷 및 데이터 확인에 대한 어려움을 설명해주세요.", key="message_check_format_before_amplification")
        message("사용자 입력", is_user=True, key="user_input_check_format_before_amplification")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_check_format_before_amplification")

    # 실습 단계 6: 데이터셋 증폭 및 최종 저장
    st.subheader("실습 단계 6: 데이터셋 증폭 및 최종 저장")
    st.markdown("질문 6: 'AI wonder' 플랫폼에서 데이터셋을 증폭하고, 증폭된 데이터셋을 저장하셨나요?")
    st.checkbox("데이터셋을 성공적으로 증폭했습니다.", key="amplify_dataset_successfully")
    st.checkbox("증폭된 데이터셋을 다시 .csv 파일로 저장했습니다.", key="save_amplified_csv")
    st.checkbox("최종 데이터셋의 구조와 내용을 검토했습니다.", key="review_final_dataset_structure")
    difficulty_review_final_dataset_structure = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_review_final_dataset_structure")
    if difficulty_review_final_dataset_structure:
        message("최종 데이터셋 구조 및 내용 검토에 대한 어려움을 설명해주세요.", key="message_review_final_dataset_structure")
        message("사용자 입력", is_user=True, key="user_input_review_final_dataset_structure")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_review_final_dataset_structure")
