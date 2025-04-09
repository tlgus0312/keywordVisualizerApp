import lib.myTextMining as tm
import lib.naverNewsCrawler as nN
from konlpy.tag import Okt




keyword =input("검색어:").strip()
resultAll = []
start=1
display=10
resultJSON = nN.searchNaverNews(keyword,start,display)

while(resultJSON != None)and(resultJSON['display']>0):
    nN.setNewsSearchResult(resultAll,resultJSON)
    start += display
    resultJSON = nN.searchNaverNews(keyword, start, display)

    if resultJSON != None:
        print(f"{keyword}[{start}:AllOk")
    else:
        print(f"{keyword}[{start}:Error]")

filename = f"./data/{keyword}_naver_news.csv"
nN.saveSearchResult_CSV(resultAll, filename)

import pandas as pd 
data_df = pd.read_csv(filename, index_col=0)
data_df



#코퍼스 로딩
input_filename= keyword + "_naver_news.csv"
corpus_list = tm.load_corpus_from_csv("./data/" +input_filename, "description")
print(corpus_list[:10])

#빈도수 추출
my_tokenizer = Okt().pos
my_tags=['Noun','Adjective','Verb']

my_stopwords=['하며','입']
counter=tm.analyze_word_freq(corpus_list, my_tokenizer, my_tags, my_stopwords)
print(list(counter.items())[:20])
tm.visualize_barchart(counter)
tm.visualize_wordcloud(counter)