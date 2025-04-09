import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc 
from wordcloud import WordCloud
def visualize_barchart(counter):
    #데이터 준비
    most_common = counter.most_common(20)

    #관심없는것은 _로 대체 
    word_list=[word for word, _ in counter.most_common(20)]
    count_list=[count for _, count in counter.most_common(20)]

    # matplotlib 한글 폰트 설정
    from matplotlib import font_manager, rc
    font_path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)

    #barh 만들기 
    fig, ax = plt.subplots()
    ax.barh(word_list[::-1], count_list[::-1])
    ax.set_xlabel("빈도수")
    ax.set_title("키워드 분석")
    return fig

def visualize_wordcloud(counter):
  from wordcloud import WordCloud
  import matplotlib.pyplot as plt

  # 한글 폰트 path 지정
  font_path = "c:/Windows/fonts/malgun.ttf"

  wordcloud = WordCloud(font_path,
                      width = 1080,
                      height = 1080,
                      max_words = 100,
                      background_color ='ivory')
  
  # 빈도 데이터로 워드클라우드 시각화
  wordcloud = wordcloud.generate_from_frequencies(counter)
  fig, ax = plt.subplots()
  ax.imshow(wordcloud, interpolation='bilinear')
  ax.axis("off")
  return fig