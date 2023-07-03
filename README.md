# Image-Crawler

### 실행방법

- GoogleImage이라는 파이썬 환경 생성: python -m venv GoogleImage

- 터미널에서 cd Scripts로 들어가서 ($ activate)로 환경 실행

- selenium 라이브러리 설치: pip install selenium

- 구글에 들어가서 chromedriver 자신의 크롬 버전과 운영체제에 맞는 버전을 환경에 압축 풀어서 설치

- google.py/naver.py에 개발자 툴에서 다운받고 싶은 이미지 검색어 searchItem에 입력

- google.py/naver.py 에 개발자 툴에서 이미지 갯수 howMany에 원하는 만큼 입력

- 해당 환경 루트로 돌아가기(cd ..)

- 구글로 스크랩할 시 python google.py 실행

- 네이버로 스크랩할 시 python naver.py 실행

### 실행결과

- searchItem 이름의 디렉토리 생성

- 그 디렉토리에 howMany 만큼의 searchItem로 구글에 검색한 이미지가 담긴다.

### 이 외

- 실행방법은 python 설치를 전제함

- 이미지 제목은 숫자고 형태는 jpg

- 주의: 다운받는 이미지 개수에 따라 시간이 걸릴 수 있음.
