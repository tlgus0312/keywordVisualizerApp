# keywordVisualizeConsoleApp.py

from lib.myTextMining import load_corpus_from_csv, analyze_word_freq
from lib.STVisualizer import visualize_barchart, visualize_wordcloud

# 더미 토크나이저 (실제 프로젝트에서는 Mecab, Okt 등을 사용)
def dummy_tokenizer(text):
    # 간단히 공백 단위로 분리하며, 모든 단어에 'NOUN' 태그 부여
    return [(word, 'NOUN') for word in text.split()]

dummy_tags = ['NOUN']
dummy_stopwords = ['은', '는', '이', '가']

def main():
    import sys
    if len(sys.argv) < 3:
        print("사용법: python keywordVisualizeConsoleApp.py <csv파일경로> <분석할컬럼명>")
        sys.exit(1)
    csv_file = sys.argv[1]
    col_name = sys.argv[2]
    
    # CSV 파일에서 텍스트 데이터를 로드
    corpus_list = load_corpus_from_csv(csv_file, col_name)
    
    # 단어 빈도 분석 수행
    counter = analyze_word_freq(corpus_list, dummy_tokenizer, dummy_tags, dummy_stopwords)
    
    # 분석 결과 콘솔에 출력
    print("상위 단어 빈도수:")
    for word, count in counter.most_common(20):
        print(f"{word}: {count}")
    
    # 시각화 결과를 Matplotlib 창으로 표시
    fig_bar = visualize_barchart(counter)
    fig_wc = visualize_wordcloud(counter)
    fig_bar.show()
    fig_wc.show()

if __name__ == "__main__":
    main()
