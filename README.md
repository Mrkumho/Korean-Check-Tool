업무상으로 일본 사업자에게 제공 하는 파일(Word 및 Excel)에 한글이 남은채로 제출 되는 경우가 종종 있음.
사업자 제출 전에 Word 및 Excel 문서에 한글이 포함 되어있 것을 확인 해주는 Tool 이 있으면 좋을 것 같다고 생각하여 만듬.

exe 파일 실행 후, word 혹은 Excel 파일을 선택하면 해당 문서에 한글이 어디에 포함되어 있는지 출력해줌.

참고 :ipynb 에서 exe 파일 만드는 방법.

=> PyInstaller로 exe 만들기 (가장 기본적인 방법)
1. PyInstaller 설치

bash
pip install pyinstaller

2. 코드가 있는 디렉토리리로 이동

bash
cd [파이썬 파일이 있는 폴더]


3. ipynb 파일을 .py 파일로 변환

bash
jupyter nbconvert --to script "Korean Check Tool.ipynb"

4. EXE 파일로 변환

bash
pyinstaller --onefile --noconsole "Korean Check Tool.py"

--onefile: 모든 파일을 하나의 exe로 만듬.
--noconsole: GUI 프로그램이라면 콘솔 창이 뜨지 않게 함.(콘솔 프로그램이면 생략 가능).

5. 완성된 exe 위치
변환이 끝나면, dist 폴더 안에 your_script.exe가 생성.


=> auto-py-to-exe (GUI로 쉽게 변환)


1. 설치

bash
pip install auto-py-to-exe

2. 실행

bash
auto-py-to-exe

3. 옵션 설정

"Script Location"에 파이썬 파일 선택
"Onefile" 체크 (하나의 exe로 만들기)
"Window Based" 선택 (GUI 프로그램일 때)
필요하면 아이콘 등 부가 설정

4. 변환 시작

"Convert .py to .exe" 버튼 클릭
변환이 끝나면 output 폴더에 exe 파일이 생깁니다.


파이썬이 깔려있지 않은 환경이어도 생성된 파일만 복사해서 사용 가능.