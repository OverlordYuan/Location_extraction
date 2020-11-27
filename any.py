import json,tqdm
import pandas as pd
with open('input/result.json','r',encoding='UTF-8') as f:
    data = json.load(f)
title = []
content = []
time = []
keyword = []
length = []
for obj in tqdm.tqdm(data):
    title.append(obj['title'])
    content.append(obj['content'])
    time.append(obj['time'])
    keyword.append(obj['keyword'])
    length.append(obj['length'])
data_df = pd.DataFrame()
data_df['title'] = title
data_df['content'] = content
data_df['time'] = time
data_df['keyword'] = keyword
data_df['length'] = length
data_df.to_excel('result.xls',encoding='utf-8')
print(data)