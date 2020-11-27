import requests,json
import pandas as pd
import tqdm,re
with open('input/dict.txt','r',encoding='utf-8') as f:
   str_ = f.readlines()

pattern = '|'.join(str_).replace('\n','')
data_df = pd.read_csv('input/query_result.csv')
result = []
result1 = []
data_list = data_df.values.tolist()
# print(data_df)
url = "http://127.0.0.1:5000/LE"
urls = "http://127.0.0.1:5000/LE_re"
res = []

for item in tqdm.tqdm (data_list):
    # title.append(item[0])
    # content.append(str(item[1]))
    data = {'title':item[0],'content':str(item[1])}
    res.append(data)
    res = requests.post(url=url,data=data).text
    # res = json.loads(res)
    # result.append(res['keyword'])
# result = {}
# result['title'] = title
# result['content'] = content
with open('input/test_data.json','w') as f:
    json.dump(res,f)
# for item in tqdm.tqdm (data_list):
#     data = {'title':item[0],'content':item[1]}
#     res = requests.post(url=urls,data=data).text
#     res = json.loads(res)
#     result1.append(res['keyword'])

print(result)
# print(result1)