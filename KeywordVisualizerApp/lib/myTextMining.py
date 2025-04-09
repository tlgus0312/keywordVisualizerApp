from collections import Counter
import pandas as pd 

def load_corpus_from_csv(corpus_file,col_name):
    data_df = pd.read_csv(corpus_file)
    result_list =list(data_df[col_name])
    return result_list

    #모았다가 제목만 디스크립션 csv 칼럼명 존재 칼람명 명시

def tokenize_korean_corpus(corpus_list,tokenizer,tags,stopwords):
    
    text_pos_list = []
    for text in corpus_list:
        #품사태깅->원하는 태깅 stopword tags를 다 받아와야됨 
        text_pos = tokenizer(text)
        text_pos_list.extend(text_pos)
    token_list =[token for token, tag in text_pos_list if tag in tags and token not in stopwords]
    return token_list
#품사태깅을 하고 리스트화 

def analyze_word_freq(corpus_list,tokenizer,tags,stopwords):
    token_list = tokenize_korean_corpus(corpus_list,tokenizer,tags,stopwords)
    counter = Counter(token_list)
    return counter

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
    import matplotlib.pyplot as plt
    plt.barh(word_list[::-1],count_list[::-1])
    # 그래프 정보 추가 
    plt.title("키워드 분석")
    plt.xlabel("빈도수")
    plt.ylabel("키워드")
    # 화면에 출력
    plt.show()

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
  plt.imshow(wordcloud)
  plt.axis('off')
  plt.show()
  