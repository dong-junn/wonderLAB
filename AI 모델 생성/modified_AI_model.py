import streamlit as st
from streamlit_chat import message


def page():
    #with st.expander("실습하기"):
        # 1. 데이터셋 업로드 절차
        st.subheader("단계 1: 데이터셋 업로드 절차")

        #st.markdown("질문 1: 'AI wonder' 웹사이트에 접속하셨나요?")
        with st.expander("질문 1: 'AI wonder' 웹사이트에 접속하셨나요?"):
            # 질문 1: 'AI wonder' 웹사이트에 접속
            question_1_1 = st.checkbox("예, 구글 크롬을 사용하여 www.ai-wonder.com에 접속했습니다.", key="key_11")
            question_1_2 = st.checkbox("예, 페이지를 한국어로 번역했습니다.", key="key_12")
            difficulty_question_1_disabled = question_1_1 and question_1_2
            difficulty_question_1 = st.checkbox("아니요, 어려움이 있습니다.", disabled=difficulty_question_1_disabled, key="checkbox1")
            if difficulty_question_1:
                message("", key="checkbox_1")
                message("", is_user=True, key="checkbox3")
                with st.container():
                    st.text_input("GPT", key="checkbox_4")

        with st.expander("질문 2: '데이터 수집' 페이지에 접근하셨나요?"):
                # 데이터 수집
                #st.markdown("질문 2: '데이터 수집' 페이지에 접근하셨나요?")
                # 데이터 수집
                all_selected_question_2 = st.checkbox("예, 'AI wonder' 메인 페이지에서 '데이터 수집' 섹션을 찾아 클릭했습니다.",
                                                      key="access_data_collection")
                difficulty_question_2_disabled = all_selected_question_2
                difficulty_question_2 = st.checkbox("아니요, 어려움이 있습니다.", disabled=difficulty_question_2_disabled,
                                                    key="difficulty_access_data_collection")

                if difficulty_question_2:
                    message("'데이터 수집' 페이지 접근에 대한 어려움을 설명해주세요.", key="message_access_data_collection")
                    message("사용자 입력", is_user=True, key="user_input_access_data_collection")
                    with st.container():
                        st.text_input("어려움을 자세히 설명해주세요", key="text_input_access_data_collection")

        with st.expander("질문 3: 데이터셋 파일을 업로드하셨나요?"):
                # 데이터셋 파일 업로드
                #st.markdown("질문 3: 데이터셋 파일을 업로드하셨나요?")
                # 데이터셋 파일 업로드
                all_selected_question_3 = st.checkbox("예, '파일찾아보기' 버튼을 클릭하여 엑셀 또는 .csv 파일을 선택하고 업로드했습니다.",
                                                      key="dataset_file_uploaded")
                difficulty_question_3_disabled = all_selected_question_3
                difficulty_question_3 = st.checkbox("아니요, 어려움이 있습니다.", disabled=difficulty_question_3_disabled,
                                                    key="difficulty_dataset_file_uploaded")
                if difficulty_question_3:
                    message("데이터셋 파일 업로드에 대한 어려움을 설명해주세요.", key="message_dataset_file_uploaded")
                    message("사용자 입력", is_user=True, key="user_input_dataset_file_uploaded")
                    with st.container():
                        st.text_input("어려움을 자세히 설명해주세요", key="text_input_dataset_file_uploaded_38")

        # 2.업로드된 데이터셋 확인

        st.subheader("단계 2: 업로드된 데이터셋 확인")

        with st.expander("질문 4: 업로드된 데이터셋이 정상적으로 표시되는지 확인하셨나요?"):
            #st.markdown("질문 4: 업로드된 데이터셋이 정상적으로 표시되는지 확인하셨나요?")

            # 업로드된 데이터셋 확인
            question_4_1 = st.checkbox("예, 페이지 하단으로 스크롤하여 업로드된 데이터셋을 확인했습니다.", key="scroll_down_uploaded_dataset")
            question_4_2 = st.checkbox("예, 모든 필요한 열과 데이터가 올바르게 나타나는지 검토했습니다.", key="review_uploaded_dataset_columns")
            difficulty_question_4_disabled = question_4_1 and question_4_2
            difficulty_question_4 = st.checkbox("아니요, 어려움이 있습니다.", disabled=difficulty_question_4_disabled,
                                                key="difficulty_review_uploaded_dataset_columns")

            if difficulty_question_4:
                message("업로드된 데이터셋 열 및 데이터 검토에 대한 어려움을 설명해주세요.", key="message_review_uploaded_dataset_columns")
                message("사용자 입력", is_user=True, key="user_input_review_uploaded_dataset_columns")
                with st.container():
                    st.text_input("어려움을 자세히 설명해주세요", key="text_input_review_uploaded_dataset_columns_52")

        # 데이터 분석 시작
        st.subheader("단계 3: 데이터 분석 시작")

        with st.expander("질문 5: '데이터 분석' 버튼을 클릭하여 기본 분석을 시작하셨나요?"):
            #st.markdown("질문 5: '데이터 분석' 버튼을 클릭하여 기본 분석을 시작하셨나요?")

            start_basic_analysis = st.checkbox("예, '데이터 분석' 버튼을 클릭하여 데이터셋에 대한 기본 분석을 수행했습니다.", key="start_basic_analysis")
            difficulty_start_basic_analysis_disabled = start_basic_analysis  # '예'가 선택되면 '아니오' 비활성화
            difficulty_start_basic_analysis = st.checkbox("아니요, 어려움이 있습니다.", disabled=difficulty_start_basic_analysis_disabled,
                                                          key="difficulty_start_basic_analysis")

            if difficulty_start_basic_analysis:
                message("기본 데이터 분석 시작에 대한 어려움을 설명해주세요.", key="message_start_basic_analysis")
                message("사용자 입력", is_user=True, key="user_input_start_basic_analysis")
                with st.container():
                    st.text_input("어려움을 자세히 설명해주세요", key="text_input_start_basic_analysis_64")

            st.markdown("질문 6: 데이터 분석의 결과를 확인하셨나요?")

            review_analysis_results = st.checkbox("예, 데이터의 개요 및 패턴을 이해하기 위해 분석 결과를 확인했습니다.", key="review_analysis_results")
            difficulty_review_analysis_results_disabled = review_analysis_results  # '예'가 선택되면 '아니오' 비활성화
            difficulty_review_analysis_results = st.checkbox("아니요, 어려움이 있습니다.",
                                                             disabled=difficulty_review_analysis_results_disabled,
                                                             key="difficulty_review_analysis_results")

            if difficulty_review_analysis_results:
                message("데이터 분석 결과 확인에 대한 어려움을 설명해주세요.", key="message_review_analysis_results")
                message("사용자 입력", is_user=True, key="user_input_review_analysis_results")
                with st.container():
                    st.text_input("어려움을 자세히 설명해주세요", key="text_input_review_analysis_results_73")

        # Target 변수 지정
        st.subheader("단계 4: Target 변수 지정")

        with st.expander("질문 7: 분석할 Target 변수를 선정하셨나요?"):
        #st.markdown("질문 7: 분석할 Target 변수를 선정하셨나요?")

            select_target_variable = st.checkbox("예, '추가 탐사 준비' 섹션에서 '관심 있는 열을 선택' 옵션을 사용하여 Target 변수를 선택했습니다.",
                                                 key="select_target_variable")
            difficulty_select_target_variable_disabled = select_target_variable  # '예'가 선택되면 '아니오' 비활성화
            difficulty_select_target_variable = st.checkbox("아니요, 어려움이 있습니다.",
                                                            disabled=difficulty_select_target_variable_disabled,
                                                            key="difficulty_select_target_variable")

            if difficulty_select_target_variable:
                message("Target 변수 선택에 대한 어려움을 설명해주세요.", key="message_select_target_variable")
                message("사용자 입력", is_user=True, key="user_input_select_target_variable")
                with st.container():
                    st.text_input("어려움을 자세히 설명해주세요", key="text_input_select_target_variable_84")



        st.divider()


        # check_completion 함수 정의
        def check_completion(*args, difficulty):
            if difficulty:
                return "gpt 도움받는 중..."
            elif all(args):
                return "완료"
            else:
                return "미입력 사항이 있음"

        # 단계 1: 질문 1, 2, 3 포함
        step1_completion = check_completion(question_1_1, question_1_2, all_selected_question_2, all_selected_question_3,
                                            difficulty=difficulty_question_1 or difficulty_question_2 or difficulty_question_3)
        st.subheader(f"단계 1: {step1_completion}")

        # 단계 2: 질문 4 포함
        step2_completion = check_completion(question_4_1, question_4_2, difficulty=difficulty_question_4)
        st.subheader(f"단계 2: {step2_completion}")

        # 단계 3: 질문 5, 6 포함
        step3_completion = check_completion(start_basic_analysis, review_analysis_results,
                                            difficulty=difficulty_start_basic_analysis or difficulty_review_analysis_results)
        st.subheader(f"단계 3: {step3_completion}")

        # 단계 4: 질문 7 포함
        step4_completion = check_completion(select_target_variable, difficulty=difficulty_select_target_variable)
        st.subheader(f"단계 4: {step4_completion}")





