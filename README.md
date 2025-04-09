# keywordVisualizerApp
크롤링을 하여 streamlit과 연동하여 cloudword와 matplotlib 그래프가 나올 수 있게 구성 

각각을 모듈화해서 코딩화하였다. 

## naverNewsCrawler.py
검색창에 검색어를 작성하면 검색창에 나오는 내용을 crawler해주는 모듈
https://developers.naver.com/main/ 네이버 개발자 센터인
Naver api로 urlib인 URL을 다루는 모듈을 작성하였다. 

## myTestMining.py



## STVisualizer.py

## KeywordVisualizeConsoleApp.py

## KeywordVisualizerSTApp.py




## 자연어처리(NLP) 단계
텍스트 전처리-> 특징 추출-> 모델 개발

NLP란, 텍스트에서 의미있는 정보를 분석, 추출하는 과정이라고 한다. 

그중 한국어 자연어처리를 위한 파이썬 라이브러리인 KoNLPy을 사용하였고, 
KoNLPy은 한국어 토큰화, 품사 태깅, 불용어 처리 등의 기능을 제공하고 있다. 

한국어는 영어와는 달리 띄어쓰기만으로 토큰화가 어렵기 때문에 
형태소 단위의 토큰화를 수행할 수 있는
KoNLPy을 사용하였다. 


