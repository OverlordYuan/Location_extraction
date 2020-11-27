import jieba, json
from flask import Flask
from flask import request
import re,time,os
from logs import TNLog
from datetime import datetime

with open('input/dict.txt','r',encoding='utf-8') as f:
    str_ = f.readlines()

pattern = '|'.join(str_).replace('\n','')
jieba.load_userdict('input/dict.txt')

with open('input/dict.json', 'r') as f:
    data = json.load(f)


def analysis(seq_list):
    res = set()
    for item in seq_list:
        if len(item)>1:
            for key in data:
                if item in data[key]:
                    if key == '2#':
                        if item[-1] == '省' or item[-1] == '市':
                            res.add(key + item[0:-1])
                        elif '自治区' in item:
                            res.add(key + item[0:2])
                        elif '内蒙古' in item:
                            res.add(key + '内蒙古')
                        elif '自治区' in item:
                            res.add(key + item[0:2])
                        else:
                            res.add(key + item)
                    elif key == '3#':
                        if '市' in item:
                            res.add(key + item[0:-1])
                        else:
                            res.add(key + item)
                    else:
                        res.add(key + item)
                    break
    return list(res)


app = Flask(__name__)

@app.route('/LE', methods=['POST'])
def LE():
    st = datetime.now()
    title = request.form['title']
    uuid = ''
    index = ''
    content = request.form['content']
    text = title + '。' + content
    seq_list = jieba.lcut(text, cut_all=False)
    entities = analysis(seq_list)
    # res = {'keyword': entities}
    # logger.info("Program version-1.3.1, Content length = "+str(len(text))+",uuid = "+ uuid +",indexName = "+ index +" ,time elapse ="+str((datetime.now() - st).microseconds)+"ms,result="+str(res)+".")
    return json.dumps(entities)

@app.route('/LE_re', methods=['POST'])
def LE_re():
    title = request.form['title']
    content = request.form['content']
    text = title + '。' + content
    seq_list = re.findall(pattern, str(text))
    entities = analysis(seq_list)
    res = {'keyword': entities}
    return json.dumps(res)


if __name__ == '__main__':
    app.run(debug=True)
