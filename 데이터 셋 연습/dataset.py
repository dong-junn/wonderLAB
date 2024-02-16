import json
import os
import streamlit as st
from streamlit_chat import message


# all_selected_step_3 = long_term_data and mid_term_data and short_term_data
# difficulty_short_term_disabled = all_selected_step_3
# difficulty_short_term = st.checkbox("아니요, 어려움이 있습니다.", disabled=difficulty_short_term_disabled,
#                                     key="difficulty_short_term")
#
# if difficulty_short_term:
#     message("단기간 데이터 수집과 관련된 어려움을 설명해주세요.")
#     message("사용자 입력", is_user=True)
#     with st.container():
#         st.text_input("어려움을 자세히 설명해주세요")




def page():


    # session_state 초기화
    # step1
    if 'datasetStep1_1' not in st.session_state:
        st.session_state.datasetStep1_1 = False

    if 'datasetStep1_2' not in st.session_state:
        st.session_state.datasetStep1_2 = False

    if 'datasetStep1_3' not in st.session_state:
        st.session_state.datasetStep1_3 = False

    if 'datasetStep1_4' not in st.session_state:
        st.session_state.datasetStep1_4 = False

    if 'datasetStep1_no' not in st.session_state:
        st.session_state.datasetStep1_no = False

    # step2
    if 'datasetStep2_1' not in st.session_state:
        st.session_state.datasetStep2_1 = False

    if 'datasetStep2_2' not in st.session_state:
        st.session_state.datasetStep2_2 = False

    if 'datasetStep2_3' not in st.session_state:
        st.session_state.datasetStep2_3 = False

    if 'datasetStep2_no' not in st.session_state:
        st.session_state.datasetStep2_no = False

    # step3
    if 'datasetStep3_1' not in st.session_state:
        st.session_state.datasetStep3_1 = False

    if 'datasetStep3_2' not in st.session_state:
        st.session_state.datasetStep3_2 = False

    if 'datasetStep3_3' not in st.session_state:
        st.session_state.datasetStep3_3 = False

    if 'datasetStep3_no' not in st.session_state:
        st.session_state.datasetStep3_no = False

    # step4
    if 'datasetStep4_1' not in st.session_state:
        st.session_state.datasetStep4_1 = False

    if 'datasetStep4_2' not in st.session_state:
        st.session_state.datasetStep4_2 = False

    if 'datasetStep4_3' not in st.session_state:
        st.session_state.datasetStep4_3 = False

    if 'datasetStep4_no' not in st.session_state:
        st.session_state.datasetStep4_no = False

   # step5
    if 'datasetStep5_1' not in st.session_state:
        st.session_state.datasetStep5_1 = False

    if 'datasetStep5_2' not in st.session_state:
        st.session_state.datasetStep5_2 = False

    if 'datasetStep5_3' not in st.session_state:
        st.session_state.datasetStep5_3 = False

    if 'datasetStep5_no' not in st.session_state:
        st.session_state.datasetStep5_no = False

    # step6
    if 'datasetStep6_1' not in st.session_state:
        st.session_state.datasetStep6_1 = False

    if 'datasetStep6_2' not in st.session_state:
        st.session_state.datasetStep6_2 = False

    if 'datasetStep6_3' not in st.session_state:
        st.session_state.datasetStep6_3 = False

    if 'datasetStep6_no' not in st.session_state:
        st.session_state.datasetStep6_no = False

    # step7
    if 'datasetStep7_1' not in st.session_state:
        st.session_state.datasetStep7_1 = False

    if 'datasetStep7_2' not in st.session_state:
        st.session_state.datasetStep7_2 = False

    if 'datasetStep7_3' not in st.session_state:
        st.session_state.datasetStep7_3 = False

    if 'datasetStep7_no' not in st.session_state:
        st.session_state.datasetStep7_no = False

    # step8
    if 'datasetStep8_1' not in st.session_state:
        st.session_state.datasetStep8_1 = False

    if 'datasetStep8_2' not in st.session_state:
        st.session_state.datasetStep8_2 = False

    if 'datasetStep8_3' not in st.session_state:
        st.session_state.datasetStep8_3 = False

    if 'datasetStep8_no' not in st.session_state:
        st.session_state.datasetStep8_no = False

    # step9
    if 'datasetStep9_1' not in st.session_state:
        st.session_state.datasetStep9_1 = False

    if 'datasetStep9_1' not in st.session_state:
        st.session_state.datasetStep9_1 = False

    if 'datasetStep9_2' not in st.session_state:
        st.session_state.datasetStep9_2 = False

    if 'datasetStep9_3' not in st.session_state:
        st.session_state.datasetStep9_3 = False

    if 'datasetStep9_no' not in st.session_state:
        st.session_state.datasetStep9_no = False

    # step10
    if 'datasetStep10_1' not in st.session_state:
        st.session_state.datasetStep10_1 = False

    if 'datasetStep10_2' not in st.session_state:
        st.session_state.datasetStep10_2 = False

    if 'datasetStep10_3' not in st.session_state:
        st.session_state.datasetStep10_3 = False

    if 'datasetStep10_no' not in st.session_state:
        st.session_state.datasetStep10_no = False

    # step11
    if 'datasetStep11_1' not in st.session_state:
        st.session_state.datasetStep11_1 = False

    if 'datasetStep11_2' not in st.session_state:
        st.session_state.datasetStep11_2 = False

    if 'datasetStep11_3' not in st.session_state:
        st.session_state.datasetStep11_3 = False

    if 'datasetStep11_no' not in st.session_state:
        st.session_state.datasetStep11_no = False



    # JSON로드
    current_dir = os.path.dirname(os.path.abspath(__file__))

    data_path = os.path.join(current_dir, 'dataset.json')

    with open(data_path, 'r', encoding='utf-8') as file:
        data = json.load(file)



    # 탭 구성 코드
    tab1, tab2 = st.tabs(["수집 실습", "작성 실습"])

    # 수집 실습 탭
    with tab1:
        st.title("데이터 수집 실습 과정")

        # step1
        st.subheader("단계 1: 주제와 관련된 데이터 유형 결정")

        with st.expander("선택한 주제와 가장 밀접하게 관련된 데이터 유형을 결정하셨나요?"):

            # 1-1
            step1_1 = st.checkbox(
                data["step1"]["checkbox1"],
                key="step1_1",
                value=st.session_state.datasetStep1_1,
            )
            st.session_state.datasetStep1_1 = step1_1

            # 1-2
            step1_2 = st.checkbox(
                data["step1"]["checkbox2"],
                key="step1_2",
                value=st.session_state.datasetStep1_2
            )
            st.session_state.datasetStep1_2 = step1_2

            # 1-3
            step1_3 = st.checkbox(
                data["step1"]["checkbox3"],
                key="step1_3",
                value=st.session_state.datasetStep1_3
            )
            st.session_state.datasetStep1_3 = step1_3

            # 1-no
            step1_selectAll = st.session_state.datasetStep1_1 and st.session_state.datasetStep1_2 and st.session_state.datasetStep1_3
            step1_no = st.checkbox(
                data["checkboxNo"],
                key="step1_no",
                value=st.session_state.datasetStep1_no,
                disabled=step1_selectAll
            )
            st.session_state.datasetStep1_no = step1_no



        # step2
        st.subheader("단계 2: 데이터 수집의 범위 설정")

        with st.expander("데이터를 수집할 범위를 어떻게 설정하셨나요?"):
            # 2-1
            step2_1 = st.checkbox(
                data["step2"]["checkbox1"],
                key="step2_1",
                value=st.session_state.datasetStep2_1
            )
            st.session_state.datasetStep2_1 = step2_1

            # 2-2
            step2_2 = st.checkbox(
                data["step2"]["checkbox2"],
                key="step2_2",
                value=st.session_state.datasetStep2_2
            )
            st.session_state.datasetStep2_2 = step2_2

            # 2-3
            step2_3 = st.checkbox(
                data["step2"]["checkbox3"],
                key="step2_3",
                value=st.session_state.datasetStep2_3
            )
            st.session_state.datasetStep2_3 = step2_3

            # 2-no
            step2_selectAll = st.session_state.datasetStep2_1 and st.session_state.datasetStep2_2 and st.session_state.datasetStep2_3
            step2_no = st.checkbox(
                data["checkboxNo"],
                key="step2_no",
                value=st.session_state.datasetStep2_no,
                disabled=step2_selectAll
            )
            st.session_state.datasetStep2_no = step2_no



        # step3
        st.subheader("단계 3: 데이터 수집의 시간적 범위 결정")

        with st.expander("질문 3: 수집할 데이터의 시간적 범위를 어떻게 설정하셨나요?"):
            # 3-1
            step3_1 = st.checkbox(
                "장기간 데이터: 지난 몇 년간의 데이터를 수집하기로 했습니다.",
                key="step3_1",
                value=st.session_state.datasetStep3_1
            )
            st.session_state.datasetStep3_1 = step3_1

            # 3-2
            step3_2 = st.checkbox(
                "중기간 데이터: 최근 몇 달간의 데이터를 수집하기로 했습니다.",
                key="step3_2",  # key 값을 'step3_2'로 설정
                value=st.session_state.datasetStep3_2
            )
            st.session_state.datasetStep3_2 = step3_2

            # 3-3
            step3_3 = st.checkbox(
                "단기간 데이터: 최근 몇 주간의 데이터를 수집하기로 했습니다.",
                key="step3_3",
                value=st.session_state.datasetStep3_3
            )
            st.session_state.datasetStep3_3 = step3_3

            # 3-no
            step3_selectAll = st.session_state.datasetStep3_1 and st.session_state.datasetStep3_2 and st.session_state.datasetStep3_3
            step3_no = st.checkbox(
                "아니요, 어려움이 있습니다.",
                key="step3_no",
                value=st.session_state.datasetStep3_no,
                disabled=step3_selectAll
            )
            st.session_state.datasetStep3_no = step3_no



        # step4
        st.subheader("단계 4: 데이터 수집 방법 선택")

        with st.expander("질문 4: 데이터를 수집할 방법을 어떻게 결정하셨나요?"):
            # 4-1
            step4_1 = st.checkbox(
                "온라인 수집: 웹 크롤링, 온라인 설문 등을 통해 데이터를 수집하기로 했습니다.",
                key="step4_1",
                value=st.session_state.datasetStep4_1
            )
            st.session_state.datasetStep4_1 = step4_1

            # 4-2
            step4_2 = st.checkbox(
                "오프라인 수집: 인터뷰, 서면 설문 등을 통해 데이터를 수집하기로 했습니다.",
                key="step4_2",
                value=st.session_state.datasetStep4_2
            )
            st.session_state.datasetStep4_2 = step4_2

            # 4-3
            step4_3 = st.checkbox(
                "혼합 방식: 온라인 및 오프라인 데이터를 조합하여 수집하기로 했습니다.",
                key="step4_3",
                value=st.session_state.datasetStep4_3
            )
            st.session_state.datasetStep4_3 = step4_3

            # 4-no
            step4_selectAll = st.session_state.datasetStep4_1 and st.session_state.datasetStep4_2 and st.session_state.datasetStep4_3
            step4_no = st.checkbox(
                "아니요, 어려움이 있습니다.",
                key="step4_no",
                value=st.session_state.datasetStep4_no,
                disabled=step4_selectAll
            )
            st.session_state.datasetStep4_no = step4_no



        # step5
        st.subheader("단계 5: 데이터 수집 후 처리 방법 결정")

        with st.expander("질문 5: 데이터 수집 후 어떤 처리 과정을 계획하고 계신가요?"):

            # 5-1
            step5_1 = st.checkbox(
                "기본 처리: 데이터를 정리하고 분류하는 기본적인 처리를 진행하기로 했습니다.",
                key="step5_1",
                value=st.session_state.datasetStep5_1
            )
            st.session_state.datasetStep5_1 = step5_1

            # 5-2
            step5_2 = st.checkbox(
                "상세한 분석: 패턴 분석, 통계적 분석 등 상세한 데이터 분석을 수행하기로 했습니다.",
                key="step5_2",
                value=st.session_state.datasetStep5_2
            )
            st.session_state.datasetStep5_2 = step5_2

            # 5-3
            step5_3 = st.checkbox(
                "고급 처리: 머신 러닝, 데이터 마이닝과 같은 고급 데이터 처리 기법을 적용하기로 했습니다.",
                key="step5_3",
                value=st.session_state.datasetStep5_3
            )
            st.session_state.datasetStep5_3 = step5_3

            # 5-no
            step5_selectAll = st.session_state.datasetStep5_1 and st.session_state.datasetStep5_2 and st.session_state.datasetStep5_3
            step5_no = st.checkbox(
                "아니요, 어려움이 있습니다.",
                key="step5_no",
                value=st.session_state.datasetStep5_no,
                disabled=step5_selectAll
            )
            st.session_state.datasetStep5_no = step5_no



        st.divider()

        # # 선택사항 표시
        # st.subheader(
        #     f"2단계: {check_completion(wide_range, medium_range, narrow_range, no_difficulty=difficulty_narrow)}")
        # st.subheader(
        #     f"3단계: {check_completion(long_term_data, mid_term_data, short_term_data, no_difficulty=difficulty_short_term)}")
        # st.subheader(
        #     f"4단계: {check_completion(online_collection, offline_collection, mixed_collection, no_difficulty=difficulty_mixed)}")
        # st.subheader(
        #     f"5단계: {check_completion(basic_processing, detailed_analysis, advanced_processing, no_difficulty=difficulty_advanced)}")

    # 작성 실습 탭
    with tab2:

        st.title("최종 데이터셋 만들기 실습 과정 ")

        # step6
        st.subheader("실습 단계 1: Target 변수 결정")

        with st.expander("질문 1: 데이터셋에서 분석하고자 하는 주요 목표인 Target 변수를 정하셨나요?"):
            # 6-1
            step6_1 = st.checkbox(
                "매출액 또는 수익을 Target 변수로 정했습니다.",
                key="step6_1",
                value=st.session_state.datasetStep6_1
            )
            st.session_state.datasetStep6_1 = step6_1

            # 6-2
            step6_2 = st.checkbox(
                "고객 만족도 또는 사용자 참여도를 Target 변수로 선정했습니다.",
                key="step6_2",
                value=st.session_state.datasetStep6_2
            )
            st.session_state.datasetStep6_2 = step6_2

            # 6-3
            step6_3 = st.checkbox(
                "제품의 품질 또는 서비스의 효율성을 중심으로 설정했습니다.",
                key="step6_3",
                value=st.session_state.datasetStep6_3
            )
            st.session_state.datasetStep6_3 = step6_3



            # 6-no
            step6_selectAll = st.session_state.datasetStep6_1 and st.session_state.datasetStep6_2 and st.session_state.datasetStep6_3
            step6_no = st.checkbox(
                "아니요, 어려움이 있습니다.",
                key="step6_no",
                value=st.session_state.datasetStep6_no,
                disabled=step6_selectAll
            )
            st.session_state.datasetStep6_no = step6_no



        # step7
        st.subheader("실습 단계 2: 주요 변수 식별")

        with st.expander("질문 2: Target 변수에 영향을 미칠 주요 변수들을 식별하고 엑셀에 기록하셨나요?"):
            # 7-1
            step7_1 = st.checkbox(
                "가격, 프로모션, 할인율과 같은 마케팅 변수를 포함했습니다.",
                key="step7_1",
                value=st.session_state.datasetStep7_1
            )
            st.session_state.datasetStep7_1 = step7_1

            # 7-2
            step7_2 = st.checkbox(
                "제품 특성, 고객 서비스의 질, 리뷰 등을 주요 변수로 기록했습니다.",
                key="step7_2",
                value=st.session_state.datasetStep7_2
            )
            st.session_state.datasetStep7_2 = step7_2

            # 7-3
            step7_3 = st.checkbox(
                "시장 동향, 경쟁사 활동, 경제 상황을 변수로 고려했습니다.",
                key="step7_3",
                value=st.session_state.datasetStep7_3
            )
            st.session_state.datasetStep7_3 = step7_3



            # 7-no
            step7_selectAll = st.session_state.datasetStep7_1 and st.session_state.datasetStep7_2 and st.session_state.datasetStep7_3
            step7_no = st.checkbox(
                "아니요, 어려움이 있습니다.",
                key="step7_no",
                value=st.session_state.datasetStep7_no,
                disabled=step7_selectAll
            )
            st.session_state.datasetStep7_no = step7_no



        # step8
        st.subheader("실습 단계 3: Target 및 주요 변수값 엑셀에 입력")

        with st.expander("질문 3: 선택한 변수들에 대해 총 30개의 값을 엑셀에 가로로 입력하셨나요?"):
            # 8-1
            step8_1 = st.checkbox(
                "각 변수에 대해 30개의 값을 직접 가로로 입력했습니다.",
                key="step8_1",
                value=st.session_state.datasetStep8_1
            )
            st.session_state.datasetStep8_1 = step8_1

            # 8-2
            step8_2 = st.checkbox(
                "실제 데이터나 가상 데이터를 모든 변수에 대해 입력했습니다.",
                key="step8_2",
                value=st.session_state.datasetStep8_2
            )
            st.session_state.datasetStep8_2 = step8_2

            # 8-3
            step8_3 = st.checkbox(
                "chatGPT에 변수명만 들어간 파일을 올리고, 가상의 값을 생성하도록 요청하여 변수값을 채웠습니다.",
                key="step8_3",
                value=st.session_state.datasetStep8_3
            )
            st.session_state.datasetStep8_3 = step8_3

            # 8-no
            step8_selectAll = st.session_state.datasetStep8_1 and st.session_state.datasetStep8_2 and st.session_state.datasetStep8_3
            step8_no = st.checkbox(
                "아니요, 어려움이 있습니다.",
                key="step8_no",
                value=st.session_state.datasetStep8_no,
                disabled=step8_selectAll
            )
            st.session_state.datasetStep8_no = step8_no



        # step9
        st.subheader("실습 단계 4: 데이터셋의 구조 확인 및 전처리")

        with st.expander("질문 4: 엑셀에서 데이터셋의 구조를 검토하고 필요한 전처리를 수행하셨나요?"):
            # 9-1
            step9_1 = st.checkbox(
                "모든 열과 행이 적절하게 배열되어 있는지 확인했습니다.",
                key="step9_1",
                value=st.session_state.datasetStep9_1
            )
            st.session_state.datasetStep9_1 = step9_1

            # 9-2
            step9_2 = st.checkbox(
                "데이터 형식과 단위가 일관되게 설정되었는지 검토했습니다.",
                key="step9_2",
                value=st.session_state.datasetStep9_2
            )
            st.session_state.datasetStep9_2 = step9_2

            # 9-3
            step9_3 = st.checkbox(
                "누락된 값이 없도록 데이터를 정제했습니다.",
                key="step9_3",
                value=st.session_state.datasetStep9_3
            )
            st.session_state.datasetStep9_3 = step9_3

            # 9-no
            step9_selectAll = st.session_state.datasetStep9_1 and st.session_state.datasetStep9_2 and st.session_state.datasetStep9_3
            step9_no = st.checkbox(
                "아니요, 어려움이 있습니다.",
                key="step9_no",
                value=st.session_state.datasetStep9_no,
                disabled=step9_selectAll
            )
            st.session_state.datasetStep9_no = step9_no



        # step10
        st.subheader("실습 단계 5: 데이터셋 저장 및 증폭 준비")

        with st.expander("질문 5: 완성된 데이터셋을 .csv 파일로 저장하고 증폭을 위해 준비하셨나요?"):
            # 10-1
            step10_1 = st.checkbox(
                "데이터셋을 .csv 형식으로 저장했습니다. 파일 이름은 영어로 작성했습니다 (예: myfile.csv).",
                key="step10_1",
                value=st.session_state.datasetStep10_1
            )
            st.session_state.datasetStep10_1 = step10_1

            # 10-2
            step10_2 = st.checkbox(
                "저장된 파일을 'AI wonder' 플랫폼에 업로드하기 위해 준비했습니다.",
                key="step10_2",
                value=st.session_state.datasetStep10_2
            )
            st.session_state.datasetStep10_2 = step10_2

            # 10-button
            st.link_button("AI wonder로 이동하기", "http://magiccanaiv2-1212047460.ap-northeast-2.elb.amazonaws.com/")

            # 10-3
            step10_3 = st.checkbox(
                "증폭 기능을 사용하기 전에 파일 포맷과 데이터를 최종 확인했습니다.",
                key="step10_3",
                value=st.session_state.datasetStep10_3
            )
            st.session_state.datasetStep10_3 = step10_3

            # 10-no
            step10_selectAll = st.session_state.datasetStep10_1 and st.session_state.datasetStep10_2 and st.session_state.datasetStep10_3
            step10_no = st.checkbox(
                "아니요, 어려움이 있습니다.",
                key="step10_no",
                value=st.session_state.datasetStep10_no,
                disabled=step10_selectAll
            )
            st.session_state.datasetStep10_no = step10_no




        # step11
        st.subheader("실습 단계 6: 데이터셋 증폭 및 최종 저장")

        with st.expander("질문 6: 'AI wonder' 플랫폼에서 데이터셋을 증폭하고, 증폭된 데이터셋을 저장하셨나요?"):
            # 11-1
            step11_1 = st.checkbox(
                "데이터셋을 성공적으로 증폭했습니다.",
                key="step11_1",
                value=st.session_state.datasetStep11_1
            )
            st.session_state.datasetStep11_1 = step11_1

            # 11-2
            step11_2 = st.checkbox(
                "증폭된 데이터셋을 다시 .csv 파일로 저장했습니다.",
                key="step11_2",
                value=st.session_state.datasetStep11_2
            )
            st.session_state.datasetStep11_2 = step11_2

            # 11-3
            step11_3 = st.checkbox(
                "최종 데이터셋의 구조와 내용을 검토했습니다.",
                key="step11_3",
                value=st.session_state.datasetStep11_3
            )
            st.session_state.datasetStep11_3 = step11_3

            # 11-no
            step11_selectAll = st.session_state.datasetStep11_1 and st.session_state.datasetStep11_2 and st.session_state.datasetStep11_3
            step11_no = st.checkbox(
                "아니요, 어려움이 있습니다.",
                key="step11_no",
                value=st.session_state.datasetStep11_no,
                disabled=step11_selectAll
            )
            st.session_state.datasetStep11_no = step11_no



        st.divider()
        # # 실습 단계 1: Target 변수 결정
        # st.subheader(
        #     f"실습 단계 1: {check_completion(target_revenue, target_customer_satisfaction, target_product_quality, difficulty=difficulty_target_product_quality)}")
        #
        # # 실습 단계 2: 주요 변수 식별
        # st.subheader(
        #     f"실습 단계 2: {check_completion(marketing_variables, product_features, market_trends, difficulty=difficulty_market_trends)}")
        #
        # # 실습 단계 3: Target 및 주요 변수값 엑셀에 입력
        # st.subheader(
        #     f"실습 단계 3: {check_completion(input_30_values, input_actual_or_simulated_data, input_values_via_chatGPT, difficulty=difficulty_input_values_via_chatGPT)}")
        #
        # # 실습 단계 4: 데이터셋의 구조 확인 및 전처리
        # st.subheader(
        #     f"실습 단계 4: {check_completion(check_columns_rows, check_data_format, clean_missing_values, difficulty=difficulty_clean_missing_values)}")
        #
        # # 실습 단계 5: 데이터셋 저장 및 증폭 준비
        # st.subheader(
        #     f"실습 단계 5: {check_completion(prepare_upload_ai_wonder, check_format_before_amplification, difficulty=difficulty_check_format_before_amplification)}")
        #
        # # 실습 단계 6: 데이터셋 증폭 및 최종 저장
        # st.subheader(
        #     f"실습 단계 6: {check_completion(amplify_dataset_successfully, review_final_dataset_structure, difficulty=difficulty_review_final_dataset_structure)}")
