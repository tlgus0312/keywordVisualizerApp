# keywordVisualizerApp
크롤링을 하여 streamlit과 연동하여 cloudword와 matplotlib 그래프가 나올 수 있게 구성 

각각을 모듈화해서 코딩화하였다. 

## naverNewsCrawler.py
검색창에 검색어를 작성하면 검색창에 나오는 내용을 crawler해주는 모듈
https://developers.naver.com/main/ 네이버 개발자 센터인
Naver api로 urlib인 URL을 다루는 모듈을 작성하였다. 

## myTestMining.py
텍스트 분석
형태소 분석**: Konlpy의 Okt 토크나이저를 사용하여 뉴스 기사 설명을 토큰화하며, 명사, 동사, 형용사 등의 지정된 품사만 선택한다.
  - **불용어 처리**: 분석 과정에서 특정 불용어(예: '하며', '입', '하고' 등)를 제거하여 분석 정확도를 높인다.
  - **단어 빈도 계산**: collections.Counter를 이용해 각 토큰의 출현 빈도를 계산한다.

## STVisualizer.py
시각화 모듈
*워드클라우드**: 수집된 단어 빈도 데이터를 기반으로 wordcloud 라이브러리를 활용해 시각화한다
  - **막대그래프**: matplotlib을 이용해 상위 N개의 단어를 수평 막대그래프로 보여준다
  - **Streamlit 통합**: STVisualize 모듈을 통해 Streamlit 앱 내에서 워드클라우드와 막대그래프를 직접 렌더링한다.

## KeywordVisualizeConsoleApp.py

사용자로부터 필요한 파라미터(예: 검색어, 최소 단어 빈도 등)를 입력받거나 미리 정의된 파라미터를 사용하여 데이터를 처리한다

## KeywordVisualizerSTApp.py
Streamlit을 기반으로 한 웹 애플리케이션 형태의 인터페이스를 제공한다.



## 자연어처리(NLP) 단계
텍스트 전처리-> 특징 추출-> 모델 개발

NLP란, 텍스트에서 의미있는 정보를 분석, 추출하는 과정이라고 한다. 

그중 한국어 자연어처리를 위한 파이썬 라이브러리인 KoNLPy을 사용하였고, 
KoNLPy은 한국어 토큰화, 품사 태깅, 불용어 처리 등의 기능을 제공하고 있다. 

한국어는 영어와는 달리 띄어쓰기만으로 토큰화가 어렵기 때문에 
형태소 단위의 토큰화를 수행할 수 있는
KoNLPy을 사용하였다. 

## Streamlit
데이터 시각화 및 분석 결과의 대시보드 제공


