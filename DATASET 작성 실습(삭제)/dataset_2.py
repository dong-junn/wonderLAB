import streamlit as st
from streamlit_chat import message


def page():
    # 실습 단계 1: Target 변수 결정
    st.subheader("실습 단계 1: Target 변수 결정")
    st.markdown("질문 1: 데이터셋에서 분석하고자 하는 주요 목표인 Target 변수를 정하셨나요?")
    st.checkbox("매출액 또는 수익을 Target 변수로 정했습니다.")
    st.checkbox("고객 만족도 또는 사용자 참여도를 Target 변수로 선정했습니다.")
    st.checkbox("제품의 품질 또는 서비스의 효율성을 중심으로 설정했습니다.")

    # 실습 단계 2: 주요 변수 식별
    st.subheader("실습 단계 2: 주요 변수 식별")
    st.markdown("질문 2: Target 변수에 영향을 미칠 주요 변수들을 식별하고 엑셀에 기록하셨나요?")
    st.checkbox("가격, 프로모션, 할인율과 같은 마케팅 변수를 포함했습니다.")
    st.checkbox("제품 특성, 고객 서비스의 질, 리뷰 등을 주요 변수로 기록했습니다.")
    st.checkbox("시장 동향, 경쟁사 활동, 경제 상황을 변수로 고려했습니다.")

    # 실습 단계 3: Target 및 주요 변수값 엑셀에 입력
    st.subheader("실습 단계 3: Target 및 주요 변수값 엑셀에 입력")
    st.markdown("질문 3: 선택한 변수들에 대해 총 30개의 값을 엑셀에 가로로 입력하셨나요?")
    st.checkbox("각 변수에 대해 30개의 값을 직접 가로로 입력했습니다.")
    st.checkbox("실제 데이터나 가상 데이터를 모든 변수에 대해 입력했습니다.")
    st.checkbox("chatGPT에 변수명만 들어간 파일을 올리고, 가상의 값을 생성하도록 요청하여 변수값을 채웠습니다.")
    message("gpt연결 예정")
    message("~~", is_user=True)
    with st.container():
        st.text_input("사용자 입력:")
    st.checkbox("실제 데이터와 추정치를 혼합하여 변수값을 완성했습니다.")



    # 실습 단계 4: 데이터셋의 구조 확인 및 전처리
    st.subheader("실습 단계 4: 데이터셋의 구조 확인 및 전처리")
    st.markdown("질문 4: 엑셀에서 데이터셋의 구조를 검토하고 필요한 전처리를 수행하셨나요?")
    st.checkbox("모든 열과 행이 적절하게 배열되어 있는지 확인했습니다.")
    st.checkbox("데이터 형식과 단위가 일관되게 설정되었는지 검토했습니다.")
    st.checkbox("누락된 값이 없도록 데이터를 정제했습니다.")

    # 실습 단계 5: 데이터셋 저장 및 증폭 준비
    st.subheader("실습 단계 5: 데이터셋 저장 및 증폭 준비")
    st.markdown("질문 5: 완성된 데이터셋을 .csv 파일로 저장하고 증폭을 위해 준비하셨나요?")
    st.checkbox("데이터셋을 .csv 형식으로 저장했습니다. 파일 이름은 영어로 작성했습니다 (예: myfile.csv).")
    st.checkbox("저장된 파일을 'AI wonder' 플랫폼에 업로드하기 위해 준비했습니다.")
    st.checkbox("증폭 기능을 사용하기 전에 파일 포맷과 데이터를 최종 확인했습니다.")

    # 실습 단계 6: 데이터셋 증폭 및 최종 저장
    st.subheader("실습 단계 6: 데이터셋 증폭 및 최종 저장")
    st.markdown("질문 6: 'AI wonder' 플랫폼에서 데이터셋을 증폭하고, 증폭된 데이터셋을 저장하셨나요?")
    st.checkbox("데이터셋을 성공적으로 증폭했습니다.")
    st.checkbox("증폭된 데이터셋을 다시 .csv 파일로 저장했습니다.")
    st.checkbox("최종 데이터셋의 구조와 내용을 검토했습니다.")








