import streamlit as st
import streamlit_antd_components as sac
import json
import importlib
import sys
import os



# 현재 스크립트의 디렉토리 경로를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)  # 현재 디렉토리를 모듈 경로에 추가합니다.

# json 로드
with open('main.json', 'r', encoding='utf-8') as file:
    main_json = json.load(file)

# Sidebar 스타일 적용
st.markdown(main_json['sidebar']['style']['markdown'], unsafe_allow_html=True)

st.markdown(main_json['sidebar']['style']['markdown'], unsafe_allow_html=True)


# st.sidebar.title("유통계산기 ver.1")
with st.sidebar.expander("Wonder_LAB", expanded=True):
    st.session_state.page = sac.menu([
        sac.MenuItem('협회소개', icon='house-fill'),
        sac.MenuItem('AI 프로젝트 안내', icon='box-fill', children=[
            sac.MenuItem('프로젝트 둘러보기', icon='apple'),
            sac.MenuItem('프로젝트 신청하기', icon='apple'),
            sac.MenuItem('3분 테스트 도전', icon='apple'),
        ]),
        sac.MenuItem('AI 프로젝트 실전', icon='box-fill', children=[
            sac.MenuItem('프로젝트 주제선택', icon='apple'),
            sac.MenuItem('나만의 AI 설계', icon='apple'),
            sac.MenuItem('효율성 판단지표 생성', icon='apple'),
            sac.MenuItem('데이터 셋 연습', icon='apple'),
            sac.MenuItem('AI 모델 생성', icon='apple'),
            sac.MenuItem('AI 적용 시뮬레이션', icon='apple'),
        ]),
        sac.MenuItem('MY 정보', icon='box-fill', children=[
            sac.MenuItem('내 프로젝트 현황(정보/등록)', icon='apple'),
            sac.MenuItem('인증서 발급', icon='apple'),
            sac.MenuItem('평가서 제출', icon='apple')
        ]),
    ], color='yellow', format_func='title', open_all=False, return_index=True)
    st.write(st.session_state)

# 현재 페이지번호 확인하는용도
st.write(f"{st.session_state.page}")



# # Sidebar 구성
# with st.sidebar:
#     with st.expander("HOME", expanded=True):
#         selected_option = option_menu(
#             main_json['sidebar']['name'],
#             options=list(main_json['pages'].keys()),
#             icons=main_json['sidebar']['icons'],
#             menu_icon=main_json['sidebar']['menu_icon'],
#             default_index=0,
#             styles={**main_json['sidebar']['style']['css']}
#         )
#         st.write(st.session_state)

# if selected_option is not None:
#     # 선택된 페이지의 소스 파일명을 가져옵니다.
#     file_name = main_json['pages'].get(selected_option)
#     if file_name:
#         # 모듈 경로를 폴더명과 소스 파일명으로부터 구성합니다.
#         module_path = f"{selected_option}.{file_name}"
#         try:
#             # 모듈을 가져옵니다.
#             module = importlib.import_module(module_path)
#             # 모듈 내의 main 함수를 호출합니다.
#             if hasattr(module, 'page'):
#                 module.page()
#
#             else:
#                 st.error(f"Error: 'main' function not found in the module '{module_path}'.")
#         except ModuleNotFoundError as e:
#             st.error(f"Module not found: {e}")
#             # 적절한 오류 메시지 또는 로그를 남기는 코드를 추가할 수 있습니다.
#     else:
#         st.error(f"No module information found for selected option: {selected_option}")
#         # 선택된 옵션에 대한 모듈 정보가 없을 때의 처리를 추가합니다.


if 'page' in st.session_state:
    # 협회소개
    if st.session_state.page == 0:
        module = importlib.import_module('협회소개.association_introduction')
        module.page()

    elif st.session_state.page == 2:
        module = importlib.import_module('프로젝트 둘러보기.project_introduction')
        module.page()

    elif st.session_state.page == 3:
        module = importlib.import_module('프로젝트 신청하기.user_information')
        module.page()

    elif st.session_state.page == 4:
        module = importlib.import_module('프로젝트 샘플보기.proj_sample')
        module.page()

    elif st.session_state.page == 6:
        module = importlib.import_module('주제 설정.select_topic')
        module.page()

    elif st.session_state.page == 7:
        module = importlib.import_module('나만의 AI 설계.project_progress')
        module.page()

    # AI 프로젝트 실전
    elif st.session_state.page == 8:
        module = importlib.import_module('효율성 판단지표 생성.efficiency_metric')
        module.page()

    elif st.session_state.page == 9:
        module = importlib.import_module('데이터 셋 연습.dataset')
        module.page()


    elif st.session_state.page == 10:
        module = importlib.import_module('AI 모델 생성.modified_AI_model')
        module.page()

    elif st.session_state.page == 11:
        module = importlib.import_module('AI 적용 시뮬레이션.apply_ai')
        module.page()

    # My 정보
    elif st.session_state.page == 13:
        # 두 번째 메뉴 아이템에 대응하는 모듈 로딩 및 실행
        module = importlib.import_module('나의 프로젝트 정보.dashboard')
        module.page()

    elif st.session_state.page == 14:
        module = importlib.import_module('인증서 발급.certification')
        module.page()

    elif st.session_state.page == 15:
        module = importlib.import_module('프로젝트 평가.evaluation')
        module.page()

else:
    st.error("No page selected.")




# session state 초기화
# 사용자 입력
if 'ai_level_selection' not in st.session_state:
    st.session_state['ai_level_selection'] = '초심자'

if 'ai_level' not in st.session_state:
    st.session_state['ai_level'] = '초심자'  # Assuming default selection

if 'activity_field' not in st.session_state:
    st.session_state['activity_field'] = '직장인'

if 'career' not in st.session_state:
    st.session_state['career'] = '~5년'

if 'detailed_student_status' not in st.session_state:
    st.session_state['detailed_student_status'] = ''

if 'selected_purposes' not in st.session_state:
    st.session_state['selected_purposes'] = []

st.session_state.selected_purposes_str = ', '.join(st.session_state.get('selected_purposes', []))
#
# # 주제 설정
if 'purpose1' not in st.session_state:
    st.session_state['purpose1'] = '강점강화'

if 'purpose2' not in st.session_state:
    st.session_state['purpose2'] = '오류 개선'

if 'work_typ' not in st.session_state:
    st.session_state['work_typ'] = '데이터로 정보를 받고 대응하는 업무'

if 'task_order' not in st.session_state:
    st.session_state['task_order'] = '업무를 모두 직접 진행'

if 'core_function' not in st.session_state:
    st.session_state['core_function'] = '예측이 필요하거나 가능한 업무'

if 'ai_advantages' not in st.session_state:
    st.session_state['ai_advantages'] = '시간 대비 생산성 향상'
#
# # AI 구현 설계
for step in ['step3', 'step4']:
    if step not in st.session_state:
        st.session_state[step] = "분류(개/고양이 구분)" if step == 'step3' else "기본 업무 단계 시각화"
#
# # 효율성 판단지표
if 'time_change' not in st.session_state:  # session_state 초기화
    st.session_state['time_change'] = ''

if 'input_before_time' not in st.session_state:  # session_state 초기화
    st.session_state['input_before_time'] = ''

if 'quality_impact' not in st.session_state:
    st.session_state['quality_impact'] = "상당히 향상"

if 'quality_measurement' not in st.session_state:
    st.session_state['quality_measurement'] = "고객 만족도"

if 'staff_change' not in st.session_state:
    st.session_state['staff_change'] = "감소"

if 'staff_management' not in st.session_state:
    st.session_state['staff_management'] = "재교육 및 재배치"

if 'procedure_impact' not in st.session_state:
    st.session_state['procedure_impact'] = "상당히 간소화"

if 'procedure_evaluation' not in st.session_state:
    st.session_state['procedure_evaluation'] = "처리 시간 단축"

if '1' not in st.session_state:
    st.session_state['1'] = ""









