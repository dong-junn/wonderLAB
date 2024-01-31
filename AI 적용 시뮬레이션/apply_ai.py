import streamlit as st
from streamlit_chat import message


def page():
    # 데이터셋 업로드 및 분석
    st.subheader("데이터셋 업로드 및 분석")

    st.markdown("질문 1: 'AI wonder'에서 데이터셋을 업로드하셨나요?")
    st.checkbox(" '데이터 수집' 페이지를 클릭했습니다.", key="clicked_data_collection_page")
    st.checkbox(" '파일찾아보기' 버튼을 눌러 저장한 파일을 업로드했습니다.", key="uploaded_file")
    st.checkbox(" 페이지 하단에서 업로드된 데이터셋이 정상적으로 보이는지 확인했습니다.", key="checked_uploaded_dataset")
    difficulty_checked_uploaded_dataset = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_checked_uploaded_dataset")
    if difficulty_checked_uploaded_dataset:
        message("업로드된 데이터셋 확인에 대한 어려움을 설명해주세요.", key="message_checked_uploaded_dataset")
        message("사용자 입력", is_user=True, key="user_input_checked_uploaded_dataset")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_checked_uploaded_dataset")

    st.markdown("질문 2: 데이터셋에 대한 분석을 수행하셨나요?")
    st.checkbox(" '데이터 분석' 버튼을 클릭했습니다.", key="clicked_data_analysis")
    st.checkbox(" '추가 탐사 준비' 섹션에서 관심 있는 열을 선택하여 Target 변수를 지정했습니다.", key="selected_target_variable")
    st.checkbox(" 타겟 변수와 다른 변수들 간의 상관관계 매트릭스를 확인했습니다.", key="checked_correlation_matrix")

    difficulty_checked_correlation_matrix = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_checked_correlation_matrix")
    if difficulty_checked_correlation_matrix:
        message("상관관계 매트릭스 확인에 대한 어려움을 설명해주세요.", key="message_checked_correlation_matrix")
        message("사용자 입력", is_user=True, key="user_input_checked_correlation_matrix")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_checked_correlation_matrix")

    # 모델 빌딩 및 평가
    st.subheader("모델 빌딩 및 평가")

    st.markdown("질문 3: 타겟 변수를 예측하는 모델을 만들기 위한 준비를 하셨나요?")
    st.checkbox(" '모델 빌딩' 버튼을 클릭했습니다.", key="clicked_model_building")
    st.checkbox(" '타겟 컬럼'에서 예측하고자 하는 타겟 변수를 선택했습니다.", key="selected_target_column")
    st.checkbox(" '마술을 해 보셔요' 버튼을 클릭하여 모델 생성을 시작했습니다.", key="clicked_start_model_creation")
    st.checkbox(" 모델 생성이 완료될 때까지 30초에서 1분 정도 기다렸습니다.", key="waited_for_model_creation")
    difficulty_waited_for_model_creation = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_waited_for_model_creation")
    if difficulty_waited_for_model_creation:
        message("모델 생성 완료 대기에 대한 어려움을 설명해주세요.", key="message_waited_for_model_creation")
        message("사용자 입력", is_user=True, key="user_input_waited_for_model_creation")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_waited_for_model_creation")

    # 모델 테스트 페이지 접근
    st.subheader("모델 테스트 페이지 접근")

    st.markdown("질문 4: '모델 테스트' 페이지에 접근하셨나요?")
    st.checkbox(" '모델 테스트'라는 페이지 버튼을 클릭했습니다.", key="clicked_model_test_page")
    difficulty_clicked_model_test_page = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_clicked_model_test_page")
    if difficulty_clicked_model_test_page:
        message("'모델 테스트' 페이지 접근에 대한 어려움을 설명해주세요.", key="message_clicked_model_test_page")
        message("사용자 입력", is_user=True, key="user_input_clicked_model_test_page")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_clicked_model_test_page")

    # 예측 방식 선택
    st.subheader("예측 방식 선택")

    st.markdown("질문 5: 예측을 위한 방식을 선택하셨나요?")
    st.checkbox(" 왼쪽 사이드 메뉴에서 '어떻게 예측하시겠습니까?' 섹션을 찾았습니다.", key="found_prediction_method_section")


    st.checkbox(" 나타나는 선택사항 중에서 '온라인'을 선택했습니다.", key="selected_online_option")
    difficulty_selected_online_option = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_selected_online_option")
    if difficulty_selected_online_option:
        message("'온라인' 선택 옵션에 대한 어려움을 설명해주세요.", key="message_selected_online_option")
        message("사용자 입력", is_user=True, key="user_input_selected_online_option")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_selected_online_option")

    # 입력값 준비 및 입력
    st.subheader("입력값 준비 및 입력")

    st.markdown("질문 6: 가상의 웹앱에 필요한 입력값을 준비하셨나요?")
    st.checkbox("오른쪽에 나타난 입력창에서, 인공지능 모델에 적용할 모든 입력값을 준비했습니다.", key="prepared_all_input_values")

    st.checkbox("가상의 웹앱에 모든 필요한 입력값을 채웠습니다.", key="filled_all_input_values")
    difficulty_filled_all_input_values = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_filled_all_input_values")
    if difficulty_filled_all_input_values:
        message("가상 웹앱의 모든 필요한 입력값 채우기에 대한 어려움을 설명해주세요.", key="message_filled_all_input_values")
        message("사용자 입력", is_user=True, key="user_input_filled_all_input_values")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_filled_all_input_values")

    # 모델 예측 수행
    st.subheader("모델 예측 수행")

    st.markdown("질문 7: 모델을 테스트하여 예측을 수행하셨나요?")
    st.checkbox(" '예측하다' 버튼을 클릭하여 모델 테스트를 진행했습니다.", key="clicked_predict_button")
    st.checkbox(" 테스트 결과가 성공적으로 산출되었습니다.", key="successful_test_result")
    difficulty_successful_test_result = st.checkbox("아니요, 어려움이 있습니다.", key="difficulty_successful_test_result")
    if difficulty_successful_test_result:
        message("테스트 결과 산출에 대한 어려움을 설명해주세요.", key="message_successful_test_result")
        message("사용자 입력", is_user=True, key="user_input_successful_test_result")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_successful_test_result")

    # 테스트 결과 저장
    st.subheader("테스트 결과 저장")

    st.markdown("질문 8: 테스트 결과를 저장하셨나요?")
    st.checkbox(" '테스트 결과 장면'을 스크린캡쳐하여 개인 PC에 저장했습니다.", key="saved_test_result_screenshot")
    difficulty_saved_test_result_screenshot = st.checkbox("아니요, 어려움이 있습니다.",
                                                          key="difficulty_saved_test_result_screenshot")
    if difficulty_saved_test_result_screenshot:
        message("테스트 결과 스크린캡쳐 저장에 대한 어려움을 설명해주세요.", key="message_saved_test_result_screenshot")
        message("사용자 입력", is_user=True, key="user_input_saved_test_result_screenshot")
        with st.container():
            st.text_input("어려움을 자세히 설명해주세요", key="text_input_saved_test_result_screenshot")

