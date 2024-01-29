import os
import streamlit as st
from PIL import Image

def page():


    mark_style = """
    <body>
    <header>
        <div class="logo-container">
            <img src="https://cdn.discordapp.com/attachments/913791234680709164/1199850385960087692/paia-logo.jpg?ex=65c40ac0&is=65b195c0&hm=44e5f1538200d32799de8166c136d9007248c8d1dafd16f7cc34dc0756586c2e&", alt="실용인공지능협회 로고">
        </div>        
        <!--<h1>실용인공지능협회</h1>-->
    </header>
    <main>
        <section id="introduction">
            <h2>소개</h2>
            <p>실용인공지능협회는 인공지능(AI) 기술의 실용적 적용에 중점을 둔 기관으로, 인공지능을 다양한 실무 환경에 통합하고 적용하는 방법을 교육하고 인증하는 데 목적을 두고 있습니다. 이 협회의 주요 목표는 이론적 지식을 넘어서 실제 업무, 연구, 일상 문제 해결에 인공지능을 적용하는 실질적인 능력을 개발하는 것입니다.</p>
        </section>
        <section id="ai-integration-project">
            <h2>실무기반 인공지능 결합 프로젝트</h2>
            <p>협회는 '실무기반 인공지능 결합 프로젝트' 프로그램을 개발하고 제공합니다. 이 프로그램은 참가자들이 실제 사업, 사무 업무, 일상의 문제, 연구 및 실험 데이터 분석, 소프트웨어 개발 등에 인공지능을 어떻게 적용할 수 있는지를 배우고, 경험하는 데 중점을 둡니다. 프로그램은 이론 교육뿐만 아니라, 참가자들이 직접 인공지능 모델을 적용해보는 실습에도 중점을 두고 있습니다.</p>
        </section>
        <section id="ai-platform">
            <h2>인공지능 모델 개발 플랫폼</h2>
            <p>협회는 자체 개발된 인공지능 모델 개발 플랫폼을 사용하여 프로젝트를 수행합니다. 이 플랫폼을 통해 참가자들은 복잡한 코딩 과정이나 인공지능 모델 개발에 대한 깊은 지식 없이도 인공지능 솔루션을 개발하고 적용할 수 있습니다. 이는 코딩 및 인공지능에 대한 지식이 전혀 없는 초보자부터, 소프트웨어 개발자들까지 다양한 수준의 참가자들이 본 프로그램을 통해 인공지능을 활용하는 능력을 배양하고 검증받을 수 있는 기회를 제공합니다.</p>
        </section>
        <section id="certification">
            <h2>인증 및 인가</h2>
            <p>본 프로젝트를 성공적으로 완료하고 긍정적인 평가를 받은 참가자들은 인증서를 수여받습니다. 이 인증서는 한국 실용인공지능협회에서 제공하며, 국가 등록된 자격기본법에 의거 정식으로 등록된 것입니다. 인증서는 참가자가 인공지능을 자신의 사업체, 업무, 연구 등에 적용하는 데 필요한 주요 능력을 갖추었음을 공식적으로 인증합니다.</p>
        </section>
        <section id="goals">
            <h2>목표 및 목적</h2>
            <p>협회는 이를 통해 실용적인 인공지능 적용 능력을 갖춘 인재를 양성함으로써, 다양한 분야에서의 혁신과 효율성 증진에 기여하고자 합니다. 이 프로젝트는 참가자들에게 인공지능이 특정 상황에서 어떻게 변혁적인 도구가 될 수 있는지에 대한 깊은 이해를 제공하며, 인공지능 기술을 실제로 적용하여 다양한 분야에서 실질적이고 측정 가능한 개선을 이루는 것을 목표로 합니다.</p>
        </section>
    </main>
    <footer>
        <p>© 2024 실용인공지능협회</p>
    </footer>
    </body>
        <style>      
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
        }

        header {
            background: #0056b3;
            color: #fff;
            padding: 1rem 0;
            text-align: center;
        }

        header h1 {
            margin: 0;
        }
        
        
        
        main {
            background: rgb(145, 223, 225);
            padding: 20px;
            
        }

        section {
            margin-bottom: 20px;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        #introduction {
            background: gray;
        }
        
        #ai-integration-project{
            background: gray;
        }
        
        #ai-platform{
            background: gray;
        }
        
        #certification{
            background: gray;
        }
        
        #goals {
            background: gray;
        }
        

        h2 {
            color: #69dc8f;
        }

        footer {
            text-align: center;
            padding: 1rem 0;
            background: #333;
            color: white;
        }
        
        .logo-container {
            text-align: center;
        }
        
        .logo-container img {
            width: 200px;
            height: auto;
        }

        @media screen and (max-width: 600px) {
            body {
                padding: 5px;
            }

            section {
                padding: 10px;
            }
        }
        
        @media screen and (max-width: 600px) {
            .logo-container img {
                with:150px;
            }
        }
    </style>
    """

    st.markdown(mark_style, unsafe_allow_html=True)
