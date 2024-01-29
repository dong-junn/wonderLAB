import streamlit as st


def page():
    mark_style = """
        <style>
        .element-container st-emotion-cache-1nx4y6e e1f1d6gn4 {
            padding-bottom: 50px;
            margin-bottom: 50px;
        }
        
        h3 {
            color: rgb(175, 209, 233);
        }
        

        </style>
    """

    st.markdown(mark_style, unsafe_allow_html=True)

    st.link_button(":rainbow[TWD로 이동하기]", "https://twd.can-ai.org/reports/")
    st.title(":green[프로젝트 개요]")
    st.subheader("제목: 인공지능의 실용적 적용과 통합 능력")
    st.subheader("목적: 참가자들에게 일반적 업무, 연구.실험 일상의 문제 해결, 소프트웨어 개발 등 다양한 분야에서 인공지능을 통합하고 적용 하는데 필요한 기술과 방법 제공")
    st.subheader(":rainbow[소요시간]: :red[4시간]")

    st.title(":green[참가자 자격]")
    st.subheader("사업주, 연구원, 고등학생, 대학생, 일상 문제 해결사, 개발자등 다양한 배경")
    st.subheader("인공지능에 대한 다양한 수준의 이해도, 초보자부터 기초 지식이 있는 사람들과 고급 지식을 가진 개발자까지")

    
    
    st.title(":green[프로젝트 단계]")
    st.subheader(":orange[인공지능 및 그 응용 소개]")
    st.subheader("ㆍ인공지능 기술과 현재 및 잠재적 응용에 대한 개요")
    st.subheader("ㆍ다양한 분야에서의 성공적인 인공지능 통합 사례연구")

    st.subheader(":orange[문제 식별 및 인공지능 솔루션 매핑]")
    st.subheader("ㆍ인공지능 솔루션이 실제 문제에 어떻게 도움이 될 수 있는지 파악")
    st.subheader("ㆍ잠재적 인공지능 응용을 자신의 업무, 사업체, 개발서비스에 적용")

    st.subheader(":orange[인공지능 솔루션 개발]")
    st.subheader("ㆍ초보자: 자신의 업무 문제에 대한 해결 도구로 인공지능 사용 안내 세션")
    st.subheader("ㆍ데이터분석능력 없는 사람: 데이터 분석 및 기본 인공지능 모델 맞춤형 교육")
    st.subheader("ㆍ개발자: 인공지능 모델 개발 및 통합에 대한 고급 모듈")

    st.subheader(":orange[실용적 응용 및 프로젝트 작업]")
    st.subheader("ㆍ배운 기술을 적용하여 식별된 문제에 대한 인공지능 기반 솔루션 직접 수행")
    st.subheader("ㆍ코딩작업 필요없이 인공지능 모델 적용 실습 섹션")

    st.subheader(":orange[결과물 제출 및 평가]")
    st.subheader("ㆍ참가자들이 직접 개발한 인공지능 솔루션을 제공 형식에 맞추어 작성 후 제출")
    st.subheader("ㆍ문제 식별, 인공지능 적용, 효율성 개선, 제출발표자료 기반으로 한 평가")

    st.title(":green[학습결과]")
    st.subheader("ㆍ실제 자신의 사업체, 업무, 연구, 개발업에서 인공지능을 어떻게 적용할 수 있는지에 대한 이해와 통찰력 확보")
    st.subheader("ㆍ개선할 수 있는 문제를 식별하고 인공지능 기반 솔루션을 직접 통합 할 수 있는 능력")
    st.subheader("ㆍ인공지능 솔루션을 개발하고 적용하는 실용적 경험")



    st.title(":green[평가기준]")
    st.subheader("통합능력: 기존 사업, 업무, 연구 개발 방식에 인공지능을 도구로 적용하는 결합 능력")
    st.subheader("실용성: 인공지능 솔루션 적용 가능한 대상을 발굴하고 실제 적용하는 능력")
    st.subheader("문제-솔루션 설계: 인공지능 통합으로 인한 새로운 프로세스나 결과의 정량적 개선 도출 능력")
    st.subheader("효율성 개선: 기존 방식 대비 인공지능 솔루션 적용한 새로운 방식 및 결과물의 효율성 평가 (소요시간, 비용, 인력, 과정, 결과물 수준)")



    st.title(":green[인증서 발급]")
    st.subheader("인증서 발급 과정은 본 프로젝트를 성공적으로 수행한 참가자들이 인공지능을 자신의 사업, 업무, 연구 등에 실질적으로 적용할 수 있는 능력을 공식적으로 인정하는 중요한 단계입니다. 이 인증서는 한국 실용인공지능협회에서 제공하며, 국가 등록된 자격기본법과 관련 법규에 의거해 정식으로 등록된 것입니다. 인증서는 참가자가 다음 세 가지 주요 능력을 갖추었음을 증명합니다")
    st.subheader("•인공지능 모델 발굴 능력 갖춤: 기존의 업무 및 방식에서 인공지능을 어떤 업무과정에 어떠한 인공지능 모델을 적용할 수 있는지 발굴하는 능력을 갖추었음")
    st.subheader("•인공지능 솔루션 설계 능력 갖춤: 기존 업무를 기반으로 인공지능 솔루션을 적용하고 설계할 수 있는 능력을 갖추었음")
    st.subheader("•효율성 계산 능력 갖춤: 인공지능이 특정 문제를 해결하거나 업무의 시간 및 비용 대비 높은 효율성을 계산할 수 있는 능력을 갖추었음")