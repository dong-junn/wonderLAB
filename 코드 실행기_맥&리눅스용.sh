#!/bin/bash

# 한글/특수문자 등의 문자 인코딩 문제 방지
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export STREAMLIT_ENABLE_PROMPT_FOR_EMAIL=false

while true; do
    clear
    echo "코드 실행기에 오신 것을 환영합니다!"
    echo
    echo "1. 최초 실행(패키지 설치 + 실행)"
    echo "2. 이후 실행(설치 미진행)"
    echo
    read -r -p "수행할 번호를 입력해주세요: " choice

    case $choice in
        1)
            echo
            echo "패키지를 설치합니다..."
            echo
            python3 -m pip install -r requirements.txt -q
            echo "설치가 완료되었습니다..."
            echo
            # 설치 후 바로 실행
            ;;
        2)
            echo
            echo "streamlit 애플리케이션을 실행합니다..."
            streamlit run main.py
            echo "실행되었습니다."
            exit
            ;;
        *)
            echo "이상한 다른 번호가 눌렸습니다. Enter를 눌러주세요..."
            read -r
            ;;
    esac
done
