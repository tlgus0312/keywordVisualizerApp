# keywordVisualizerSTApp.py

import streamlit as st
import pandas as pd
from lib.myTextMining import load_corpus_from_csv, analyze_word_freq
from lib.naverNewsCrawler import searchNaverNews, setNewsSearchResult, saveSearchResult_CSV
from lib.STVisualizer import visualize_barchart, visualize_wordcloud

# 더미 토크나이저 (실제 프로젝트에서는 형태소 분석기 사용)
def dummy_tokenizer(text):
    return [(word, 'NOUN') for word in text.split()]

dummy_tags = ['NOUN']
dummy_stopwords = ['은', '는', '이', '가']

st.title("키워드 시각화 앱")

# 사이드바 모드 선택: CSV 분석 또는 네이버 뉴스 크롤링
mode = st.sidebar.radio("모드 선택", ("CSV 분석", "네이버 뉴스 크롤링"))

if mode == "CSV 분석":
    st.header("CSV 파일을 통한 텍스트 분석")
    uploaded_file = st.file_uploader("CSV 파일 업로드", type="csv")
    if uploaded_file is not None:
        col_name = st.text_input("분석할 컬럼명 입력", value="content")
        if st.button("분석 시작"):
            corpus_list = load_corpus_from_csv(uploaded_file, col_name)
            counter = analyze_word_freq(corpus_list, dummy_tokenizer, dummy_tags, dummy_stopwords)
            st.subheader("바 차트")
            fig_bar = visualize_barchart(counter)
            st.pyplot(fig_bar)
            st.subheader("워드클라우드")
            fig_wc = visualize_wordcloud(counter)
            st.pyplot(fig_wc)

elif mode == "네이버 뉴스 크롤링":
    st.header("네이버 뉴스 크롤링 및 분석")
    keyword = st.text_input("뉴스 검색 키워드 입력")
    start = st.number_input("시작 번호", min_value=1, value=1)
    display = st.number_input("출력 건수", min_value=1, value=10)
    if st.button("크롤링 및 분석 시작"):
        if keyword:
            resultAll = []
            resultJSON = searchNaverNews(keyword, start, display)
            if resultJSON:
                setNewsSearchResult(resultAll, resultJSON)
                st.write("크롤링 결과", pd.DataFrame(resultAll))
                if st.checkbox("CSV 파일로 저장"):
                    saveSearchResult_CSV(resultAll, "naver_news.csv")
                col_name = st.text_input("분석할 컬럼명 입력", value="title")
                if st.button("분석 시작"):
                    corpus_list = [item[col_name] for item in resultAll]
                    counter = analyze_word_freq(corpus_list, dummy_tokenizer, dummy_tags, dummy_stopwords)
                    st.subheader("바 차트")
                    fig_bar = visualize_barchart(counter)
                    st.pyplot(fig_bar)
                    st.subheader("워드클라우드")
                    fig_wc = visualize_wordcloud(counter)
                    st.pyplot(fig_wc)
        else:
            st.error("뉴스 검색 키워드를 입력해주세요.")
