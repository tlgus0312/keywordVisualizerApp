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


  