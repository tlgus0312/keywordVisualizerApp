import urllib.request
import json
import pandas as pd 

def searchNaverNews(keyword, start, display):
    client_id="DrQl52mvUfRfnzIEBXKW"
    client_secret = "tyQAVEuvtx"
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과
    new_url = url + f"&start={start}&display={display}"
    request = urllib.request.Request(new_url)
    request.add_header("X-Naver-Client-ID",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    resultJSON =None
    try:
        response = urllib.request.urlopen(request)
        rescode= response.getcode()
        if(rescode==200):
            response_body= response.read()
            resultJSON= json.loads(response_body.decode('utf-8'))
    except Exception as e:
        print(e)
        print(f"Error:{new_url}")
    return resultJSON

def setNewsSearchResult(resultAll, resultJSON):
    for result in resultJSON["items"]:
        resultAll.append(result)

def saveSearchResult_CSV(json_list, filename):
    data_df =pd.DataFrame(json_list)
    data_df.to_csv(filename)
    print(f"{filename}SAVED")


