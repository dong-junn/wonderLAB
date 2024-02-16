@echo off
chcp 65001
set STREAMLIT_ENABLE_PROMPT_FOR_EMAIL=false

:start
cls
echo 코드 실행기에 오신 것을 환영합니다!
echo.

echo 1. 최초 실행(패키지 설치 + 실행)
echo 2. 이후 실행(설치 미진행)
echo.

echo 수행할 번호를 입력해주세요:
set /p choice=

if "%choice%"=="1" goto install_run
if "%choice%"=="2" goto run_only
echo 이상한 다른 번호가 눌렸습니다 Enter를 눌러주세요...
pause
goto start

:install_run
echo.
echo 패키지를 설치합니다...
echo.
python -m pip install -r requirements.txt -q
echo 설치가 완료되었습니다...
echo.
goto run_only

:run_only
echo.
echo streamlit 애플리케이션을 실행합니다...
streamlit run main.py
echo 실행되었습니다.
goto end

:end
pause

