# # coding:utf-8
import json
import os
path = 'config'
country = ['中国']
province = []
city  = []
county = []
for filename in os.listdir(path):
    print(filename)
    file_path = path+'/'+filename
    province.append(filename)
    if filename in ['北京','天津','上海','重庆']:
        province.append(filename+'市')
    elif filename  in ['香港','澳门']:
        province.append(filename+'特别行政区')
    elif filename in ['新疆','西藏','广西','宁夏','内蒙古']:
        if filename == '新疆':
            province.append('新疆维吾尔族自治区')
        elif filename == '西藏':
            province.append('西藏自治区')
        elif filename == '广西':
            province.append('广西壮族自治区')
        elif filename == '宁夏':
            province.append('宁夏回族自治区')
        else:
            province.append('内蒙古自治区')
    else:
        province.append(filename+'省')
    for json_file in os.listdir(file_path):
        json_path = file_path+'/'+json_file
        name = json_file.split('.')[0]
        if name not in ['北京','天津','上海','重庆','台湾','香港','澳门']:
            city.append(name)
            if name[-1] == '市'and len(name)>2:
                city.append(name[0:-1])
            with open(json_path,'r',encoding='utf-8') as f:
                line = f.readline()
            data = json.loads(line)
            feature = data['features']
            for obj in feature:
                properties = obj['properties']
                item = properties['name']
                if len(item)==2 and '区' in item:
                    continue
                else:
                    county.append(item)
        else:
            with open(json_path,'r',encoding='utf-8') as f:
                line = f.readline()
            data = json.loads(line)
            feature = data['features']
            for obj in feature:
                properties = obj['properties']
                item = properties['name']
                city.append(item)
                if item[-1] == '市'and len(item)>2:
                    city.append(item[0:-1])

for filename in os.listdir('input/other'):
    temp = filename.split('.')
    city.append(temp[0])
with open('input/国家.txt','r',encoding='utf-8') as f:
    line = f.readlines()
for obj in line:
    country.append(obj.replace('\n',''))
name = {}
name['1#'] = country
name['2#'] = province
name['3#'] = city
name['4#'] = county
with open('input/dict.json','w') as f:
    json.dump(name,f)
print(1)

ad_list = []
with open('input/dict.json','r') as f:
    data = json.load(f)
for name in data:
    temp = data[name]
    ad_list += temp
print(ad_list)
with open('input/dict.txt','w',encoding='utf-8') as f:
    for obj in ad_list:
        f.writelines(obj+'\n')
